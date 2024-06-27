// 5-subscriber.js

import redis from 'redis';

// Create a Redis client
const subscriber = redis.createClient();

// On connect, log the message
subscriber.on('connect', () => {
    console.log('Redis client connected to the server');
});

// On error, log the error message
subscriber.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`);
});

// Subscribe to the channel 'holberton school channel'
subscriber.subscribe('holberton school channel');

// Handle incoming messages
subscriber.on('message', (channel, message) => {
    console.log(message);

    // Unsubscribe and quit if message is 'KILL_SERVER'
    if (message === 'KILL_SERVER') {
        subscriber.unsubscribe();
        subscriber.quit();
    }
});

