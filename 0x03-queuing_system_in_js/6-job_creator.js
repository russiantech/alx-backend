// 6-job_creator.js

import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Object containing the Job data format
const jobData = {
    phoneNumber: '1234567890',
    message: 'This is the code to verify your account',
};

// Create a job in the 'push_notification_code' queue
const job = queue.create('push_notification_code', jobData);

// Event listeners for job creation
job.on('enqueue', function() {
    console.log(`Notification job created: ${job.id}`); // Use job.id to get the job ID
});

job.on('complete', function() {
    console.log('Notification job completed');
});

job.on('failed', function() {
    console.log('Notification job failed');
});

// Save the job to the queue
job.save();

