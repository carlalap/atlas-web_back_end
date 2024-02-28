//import kue from 'kue';
// const queue = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) { 
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }

    jobs.forEach((job) => {
        const pushNotificationJob = queue.create('push_notification_code_3', job);

        pushNotificationJob.save ((error) => {
            if (!error) console.log(`Notification job created: ${pushNotificationJob.id}`);
          });

        pushNotificationJob.on('complete', () => {
            console.log(`Notification job ${pushNotificationJob.id} completed`);
        }); 

        pushNotificationJob.on('failed', (error) => {
            console.log(`Notification job ${pushNotificationJob.id} failed: ${error}`);
        }); 

        pushNotificationJob.on('progress', (progress) => {
            console.log(`Notification job ${pushNotificationJob.id} ${progress}% complete`);
        }); 

    });
};
export default createPushNotificationsJobs;
