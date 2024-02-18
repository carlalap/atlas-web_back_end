const sinon = require('sinon');
const expect = require('chai').expect;
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment.js');

describe('sendPaymentRequestToApi', function() {
  const stubUtils;
  const spyConsole;

  beforeEach(() => {
    // Create a Stub  & returns value for Utils.calculateNumber
    stubUtils = sinon.stub(Utils, 'calculateNumber').returns(10);
    // Create a spy for console.log
    spyConsole = sinon.spy(console, 'log');
  });

  afterEach(() => {
    // Restore the stub and the spy
    stubUtils.restore();
    spyConsole.restore();
  });

  it('should call Utils.calculateNumber with the correct arguments and log the result', function() {
    // call the function
    sendPaymentRequestToApi(100, 20);
    // Verify that Utils.calculateNumber was called with the correct arguments
    expect(stubUtils.calledWith('SUM', 100, 20)).to.be.true;
     // check that the stub always return the same number 10
    expect(stubUtils.alwaysReturned(10)).to.be.true;
    // Verify that console.log was called with the correct message
    expect(spyConsole.calledWith('The total is: 10')).to.be.true;
  });
});
