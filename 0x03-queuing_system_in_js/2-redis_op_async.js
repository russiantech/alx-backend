import redis from 'redis';
import { promisify } from 'util';

// Connect to Redis
const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`);
});

// Promisify Redis client methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Function to set a new school
async function setNewSchool(schoolName, value) {
    try {
        await setAsync(schoolName, value);
        console.log(`Reply: OK`);
    } catch (error) {
        console.error(`Error setting value for ${schoolName}: ${error}`);
    }
}

// Async function to display the value of a school
async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName);
        console.log(value);
    } catch (error) {
        console.error(`Error retrieving value for ${schoolName}: ${error}`);
    }
}

// Test calls
async function runTests() {
    await displaySchoolValue('Holberton');
    await setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
    client.quit(); // Quit client connection after operations
}

runTests();

