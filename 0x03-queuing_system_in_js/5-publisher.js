// 5-publisher.js

import redis from 'redis';

// Create a Redis client
const publisher = redis.createClient();

// On connect, log the message
publisher.on('connect', () => {
    console.log('Redis client connected to the server');
});

// On error, log the error message
publisher.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`);
});

// Function to publish a message after a specified time
function publishMessage(message, time) {
    setTimeout(() => {
        console.log(`About to send ${message}`);
        publisher.publish('holberton school channel', message);
    }, time);
}

// Publish messages as specified
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);

