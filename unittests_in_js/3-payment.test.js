const chai = require('chai');
const sinon = require('sinon');

const Utils = require('./utils.js');
const sendPaymentRequestToApi = require('./3-payment.js');
const { expect } = require('chai');

describe('sendPaymentRequestToApi function', () => {
  const spyUtil = sinon.spy(Utils, 'calculateNumber');

  it('validate the usage of the Utils function', () => {
    sendPaymentRequestToApi(100, 20);
    expect(spyUtil.calledOnce).to.be.true;
    expect(spyUtil.calledWith('SUM', 100, 20)).to.be.true;
    spyUtil.restore()
  });
});
