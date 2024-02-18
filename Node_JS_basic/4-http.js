// task4. Create a small HTTP server using Node's HTTP module
// Script that creates a small HTTP server using the http module:
// https://www.w3schools.com/nodejs/met_http_createserver.asp

const http = require('http');

const port = 1245;

const app = http.createServer((request, response) => {
  response.statusCode = 200;
  response.setHeader('Content-Type', 'text/plain');
  response.write('Hello Holberton School!'); // print message
  response.end();
});
app.listen(port);
module.exports = app;
