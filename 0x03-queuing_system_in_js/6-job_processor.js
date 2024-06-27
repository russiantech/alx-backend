// 6-job_processor.js

import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Function to send notification
function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process jobs in the 'push_notification_code' queue
queue.process('push_notification_code', (job, done) => {
    // Extract data from the job
    const { phoneNumber, message } = job.data;

    // Call sendNotification function
    sendNotification(phoneNumber, message);

    // Job processing completion callback
    done();
});

// Log when the queue is ready to process jobs
queue.on('ready', () => {
    console.log('Job processor is ready and listening for jobs...');
});

// Log errors if they occur
queue.on('error', (err) => {
    console.error('Queue error:', err);
});

