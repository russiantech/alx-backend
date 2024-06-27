// 4-redis_advanced_op.js

import redis from 'redis';

// Connect to Redis
const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`);
});

// Function to create a hash in Redis
function createHash() {
    client.hset(
        'HolbertonSchools',
        'Portland',
        '50',
        redis.print
    );
    client.hset(
        'HolbertonSchools',
        'Seattle',
        '80',
        redis.print
    );
    client.hset(
        'HolbertonSchools',
        'New York',
        '20',
        redis.print
    );
    client.hset(
        'HolbertonSchools',
        'Bogota',
        '20',
        redis.print
    );
    client.hset(
        'HolbertonSchools',
        'Cali',
        '40',
        redis.print
    );
    client.hset(
        'HolbertonSchools',
        'Paris',
        '2',
        redis.print
    );
}

// Function to display the hash stored in Redis
function displayHash() {
    client.hgetall('HolbertonSchools', (err, obj) => {
        if (err) {
            console.error(`Error retrieving hash: ${err}`);
        } else {
            console.log(obj);
        }
        client.quit(); // Quit client connection after operations
    });
}

// Perform operations
createHash();
displayHash();

