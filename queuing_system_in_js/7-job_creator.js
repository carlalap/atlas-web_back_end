import kue from 'kue';

const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153518743',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153538781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153118782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4159518782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4158718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153818782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4154318781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4151218782',
      message: 'This is the code 4321 to verify your account'
    }
  ];

  const queue = kue.createQueue();
  
  for (const j of jobs) {
    // Create a new job to the queue with const job: push_notification_code_2
    // If there is no error, log to the console Notification job created: JOB_ID
    const job = queue.create('push_notification_code_2', j).save((error) => {
        if (!error) console.log(`Notification job created: ${job.id}`);
    });
    // On the job completion, log to the console Notification job JOB_ID completed
    job.on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
    });
    // On the job failure, log to the console Notification job JOB_ID failed: ERROR
    job.on('failed', (error) => {
        console.log(`Notification job ${job.id} failed: ${error}`);
    });
    // On the job progress, log to the console Notification job JOB_ID PERCENTAGE% complete
    job.on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
    });
}
