import kue from 'kue';
const queue = kue.createQueue();

const blacklistedPhones = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
    if (blacklistedPhones.includes(phoneNumber)) {
        return done(Error(`Phone number ${phoneNumber} is blacklisted`));
    }
    job.progress(50, 100);
        console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
        done(); 
}

const queueName = 'push_notification_code_2';

queue.process(queueName, 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
