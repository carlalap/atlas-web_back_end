const sinon = require('sinon');
const chai = require('chai');
const expect = chai.expect;
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
      expect(spyConsole.calledOnceWithExactly('The total is: 120')).to.be.true;
    });
  })