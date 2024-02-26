/* 8. Basic Integration testing
* suite test for the index page
*/
const request = require('request');
const { expect } = require('chai');


describe('Suite test', () => {
    describe('GET /', () => {
        it('Code: 200 | Body: Welcome to the payment system', (done) => {
            const options = {
                url: 'http://localhost:7865',
                method: 'GET',
            };
            request(options, function (error, response, body) {
                expect(response.statusCode).to.equal(200);
                expect(body).to.equal('Welcome to the payment system');
                done();
              });
            });
          });
});