const sinon = require('sinon');
const expect = require('chai').expect;
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', function() {
  let spyUtils;

  beforeEach(() => {
    spyUtils = sinon.spy(Utils, 'calculateNumber');
  });

  afterEach(() => {
    spyUtils.restore();
  });

  it('should call Utils.calculateNumber with the correct arguments and log the result', function() {
    sendPaymentRequestToApi(100, 20);
    expect(spyUtils.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
  });
});
