const sinon = require('sinon');
const expect = require('chai').expect;
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', function() {
  let stubUtils;
  let spyConsole;

  beforeEach(() => {
    // Create a Stub for Utils.calculateNumber
    stubUtils = sinon.stub(Utils, 'calculateNumber');
    // Stub the return value of Utils.calculateNumber
    stubUtils.returns(10)
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
    expect(stubUtils.calledOnce).to.be.true;
    expect(stubUtils.calledWith('SUM', 100, 20)).to.be.true;

    expect(spyConsole.calledOnce).to.be.true;
    expect(spyConsole.calledWith('SUM', 100, 20)).to.be.true;
  });
});
