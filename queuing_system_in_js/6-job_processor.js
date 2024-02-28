import kue from 'kue';

const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

const queueName = 'push_notification_code';

queue.process(queueName, (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message);
    done();
});
