import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    queue = kue.createQueue();
    kue.Job.rangeByType('push_notification_code_3', 'active', 0, -1, 'asc', (err, jobs) => {
      jobs.forEach((job) => {
        job.remove(() => {});
      });
    });
  });

  beforeEach(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('should create two new jobs to the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });
});

