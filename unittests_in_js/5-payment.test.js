const sinon = require('sinon');
const expect = require('chai').expect;
const sendPaymentRequestToApi = require('./5-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', function() {
  let spyConsole;

  beforeEach(() => {
    spyConsole = sinon.spy(console, 'log');
  });

  afterEach(() => {
    spyConsole.restore();
  });

  it('should call Utils.calculateNumber with the correct arguments and log the result', function() {
    sendPaymentRequestToApi(100, 20);
    expect(spyConsole.calledOnceWithExactly('The total is: 120')).to.be.true;
  });

  it('should call Utils.calculateNumber with the correct arguments and log the result', function() {
    sendPaymentRequestToApi(10, 10);
    expect(spyConsole.calledOnceWithExactly('The total is: 20')).to.be.true;
  });
});
