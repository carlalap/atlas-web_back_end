const sinon = require('sinon');
const chai = require('chai');
const expect = chai.expect;

const sendPaymentRequestToApi = require('./3-payment.js');
const Utils = require('./utils.js');

describe('sendPaymentRequestToApi', function() {
    it('sendPaymentRequestToApi(100, 20) is the same Utils.calculateNumber(\'SUM\', 100, 20)', function() {
        const spyUtils = sinon.spy(Utils, 'calculateNumber');
        const spyConsole = sinon.spy(console, 'log');

        sendPaymentRequestToApi(100, 20);
        
        expect(spyUtils.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
        expect(spyConsole.calledOnceWithExactly('The total is: 120')).to.be.true;

        Utils.calculateNumber.restore();
        console.log.restore();
    });
});
