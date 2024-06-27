const express = require('express');
const redis = require('redis');
const { promisify } = require('util');
const kue = require('kue');

// Create Express app
const app = express();
const port = 1245;

// Create Redis client and promisify get/set functions
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Kue queue
const queue = kue.createQueue();

// Initial number of seats
const INITIAL_SEATS = 50;

// Set initial available seats and reservation flag
let reservationEnabled = true;

// Reserve seat function
async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

// Get current available seats function
async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return seats ? parseInt(seats) : null;
}

// Set initial number of available seats
reserveSeat(INITIAL_SEATS);

// Route to get the number of available seats
app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats });
});

// Route to reserve a seat
app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (errMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errMessage}`);
  });
});

// Route to process the queue
app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const currentSeats = await getCurrentAvailableSeats();
    if (currentSeats <= 0) {
      reservationEnabled = false;
      return done(new Error('Not enough seats available'));
    }

    await reserveSeat(currentSeats - 1);

    if (currentSeats - 1 === 0) {
      reservationEnabled = false;
    }

    done();
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

