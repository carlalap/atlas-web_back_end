/* task8. Basic INtegration testing
* using express
*/
const express = require('express');
const { request } = require('http');

const app = express();
const port = 7865;

app.get('/', (request, response) => {
    response.end('Welcome to the payment system');
});

app.listen(port, () => {
    console.log('API available on localhost port 7865');
});
