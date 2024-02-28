import createPushNotificationsJobs from './8-job';
import kue from 'kue';
import { expect } from 'chai';

const queue = kue.createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
];

describe('createPushNotificationsJobs', () => {
    before(function () {
      queue.testMode.enter();
    });
  
    afterEach(function () {
      queue.testMode.clear();
    });
  
    after(function () {
      queue.testMode.exit();
    });

    it('display a error message if jobs is not an array passing Number', () => {
        expect(() => {
          createPushNotificationsJobs(2, queue);
        }).to.throw('Jobs is not an array');
    });

    it('display a error message if jobs is not an array passing Object', () => {
        expect(() => {
          createPushNotificationsJobs({}, queue);
        }).to.throw('Jobs is not an array');
      });

});