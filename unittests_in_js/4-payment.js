const Utils = require('./utils');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
    const message = Utils.calculateNumber('SUM', totalAmount, totalShipping);
    console.log(`The total is: $ { message }`);
};
module.exports = sendPaymentRequestToApi;
