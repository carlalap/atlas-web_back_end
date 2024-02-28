const getPaymentTokenFromAPI = require('./6-payment_token');

const { expect } = require('chai');

describe('getPaymentTokenFromApi', () => {
    it('Returns a promise with the correct object value', (done) => {
        getPaymentTokenFromAPI(true)
        .then((response) => {
          expect(response).to.include({ data: 'Successful response from the API' });
          done();
        })
        .catch((error) => done(error));
    });
});