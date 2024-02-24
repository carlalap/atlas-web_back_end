const sinon = require('sinon');
const Utils = require('./utils');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./3-payment');


describe('sendPaymentRequestToApi', () => {
          
    it('should call Utils.calculateNumber with the correct arguments and log the result', function() {
      let spyUtils;
      sendPaymentRequestToApi(100, 20);
      expect(spyUtils.calculateNumber.calledWith('SUM', 100, 20)).to.be.true;
      expect(spyConsole.calculateNumber.callCount).to.be.equal(1);
      spyUtils.calculateNumber.restore();
    });
  });