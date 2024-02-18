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

    describe('GET /cart/12', () => {
      it('Responds with correct status 200 and id number 12 in msg', (done) => {
        const options = {
          url: 'http://localhost:7865/cart/12',
          method: 'GET',
        };

        request(options, function(error, response, body) {
          expect(response.statusCode).to.equal(200);
          expect(body).to.equal('Payment methods for cart 12');
          done();  
        });
      });
    });

    describe('GET /cart/321', () => {
      it('Responds with OK 200 and id 321 in msg', (done) => {
        const options = {
          url: 'http://localhost:7865/cart/321',
          method: 'GET',
        };

        request(options, function(error, response, body) {
          expect(response.statusCode).to.equal(200);
          expect(body).to.equal('Payment methods for cart 321');
          done();           
        });
      });
    });

    describe('GET /cart/b12', () => {
      it('Responds with error 404', (done) => {
        const options = {
          url: 'http://localhost:7865/cart/b12',
          method: 'GET',
        };
  
        request(options, function (error, response, body) {
          expect(response.statusCode).to.equal(404);
          done();
        });
      });
    });

    describe('GET /cart/12b', () => {
      it('Responds with error 404', (done) => {
        const options = {
          url: 'http://localhost:7865/cart/12b',
          method: 'GET',
        };
  
        request(options, function (error, response, body) {
          expect(response.statusCode).to.equal(404);
          done();
        });
      });
    });
  
    describe('GET /cart/hello', () => {
      it('Responds with error 404', (done) => {
        const options = {
          url: 'http://localhost:7865/cart/hello',
          method: 'GET',
        };
  
        request(options, function (error, response, body) {
          expect(response.statusCode).to.equal(404);
          done();
        });
      });
    });

});    