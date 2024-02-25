const sinon = require('sinon');
const { expect } = require('chai'); //Import 'expect' from 'chai'

const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');


describe('sendPaymentRequestToApi function', () => {
  const spyUtil = sinon.spy(Utils, 'calculateNumber');

  it('should call Utils.calculateNumber with the correct arguments and log the result', () => {
    sendPaymentRequestToApi(100, 20);
    expect(spyUtil.calledOnce).to.be.true;
    expect(spyUtil.calledWith('SUM', 100, 20)).to.be.true;
    spyUtil.restore()
  });
});
