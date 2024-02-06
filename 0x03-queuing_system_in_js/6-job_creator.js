import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '0123456789',
  message: 'This is a notification!',
};

const job = queue.create('push_notification_code', jobData);

job
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  })

  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed', () => {
    console.error('Notification job failed');
  });
