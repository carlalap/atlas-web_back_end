const Utils = require('./utils.js');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
    const message = Utils.calculateNumber('SUM', totalAmount, totalShipping);
    console.log(`The total is: $ { message }`);
};
module.exports = sendPaymentRequestToApi;
