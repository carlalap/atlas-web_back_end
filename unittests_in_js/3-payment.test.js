const sinon = require('sinon');
const chai = require('chai')
const expect = chai.expect;


const sendPaymentRequestToApi = require('./3-payment.js');
const Utils = require('./utils.js');

describe('sendPaymentRequestToApi', function() {
    it('sendPaymentRequestToApi(100, 20) is the same Utils.calculateNumber(\'SUM\', 100, 20)', function() {
        sinon.spy(Utils, 'calculateNumber');
        sendPaymentRequestToApi(100, 20);
        expect(Utils.calculateNumber.calledOnce).to.be.true;
    });
});
