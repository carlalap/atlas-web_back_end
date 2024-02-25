// task6. 6. Async tests with done - -payment_token.
function getPaymentTokenFromAPI(success) {
    if (success === true) {
        return Promise.resolve({data: 'Successful response from the API' });
    }
    return null;
};
module.exports = getPaymentTokenFromAPI;

