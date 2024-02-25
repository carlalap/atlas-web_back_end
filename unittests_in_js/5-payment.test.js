const sinon = require('sinon');
const expect = require('chai').expect;
const sendPaymentRequestToApi = require('./5-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', function() {
  let spyConsole;

  beforeEach(() => {
    // Create a spy for console.log
    spyConsole = sinon.spy(console, 'log');
  });

  afterEach(() => {
    // Restore the stub and the spy
    expect(spyConsole.calledOnce).to.be.true;
    spyConsole.restore();
  });

  it('checks output arguments with 100, and 20', function() {
    // Call the function
    sendPaymentRequestToApi(100, 20);
    expect(spyConsole.calledWith('The total is: 120')).to.be.true;
    });

  it('checks output arguments with 10, and 10', function() {
    // Verify that Utils.calculateNumber was called with the correct arguments
    sendPaymentRequestToApi(10, 10);
    expect(spyConsole.calledWith('The total is: 20')).to.be.true;
  });
});
