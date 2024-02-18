/* task10. Basic INtegration testing
* using express
*/
const express = require('express');
const { request } = require('http');

const app = express();
const port = 7865;

app.use(express.json());

app.get('/', (request, response) => {
    response.end('Welcome to the payment system');
});

app.get('/cart/:id([0-9]+)', (request, response) => {
    response.end(`Payment methods for cart ${request.params.id}`);
});

app.get('/available_payments', (request, response) => {
    const object = {
        payment_methods: {
          credit_cards: true,
          paypal: false
        },
    };
    response.json(object);
});

app.post('/login', (request, response) => {
    const username = request.body.userName;
    response.end(`Welcome ${username}`);
});


app.listen(port, () => {
    console.log(`API available on localhost port ${port}`);
});
