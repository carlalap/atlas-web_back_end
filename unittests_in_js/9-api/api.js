/* task9. Basic INtegration testing
* using express
*/
const express = require('express');
const { request } = require('http');

const app = express();
const port = 7865;


app.get('/', (request, response) => {
    response.end('Welcome to the payment system');
});

app.get('/cart/:id([0-9]+)', (request, responde) => {
    responde.end(`Payment methods for cart ${request.params.id}`);
});

app.listen(port, () => {
    console.log('API available on localhost port 7865');
});
