const getPaymentTokenFromAPI = require('./6-payment_token');
const { expect } = require('chai');

describe('getPaymentTokenFromApi', () => {
    it('Returns promise with the object value correctly', (done) => {
        getPaymentTokenFromAPI(True)
        .then((response) => {
          expect(response).to.include({ data: 'Successful response from the API' });
          done();
        })
        .catch((error) => done(error));
    });
});