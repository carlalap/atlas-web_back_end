// task4. Create a small HTTP server using Node's HTTP module
// Script that creates a small HTTP server using the http module:
// https://www.w3schools.com/nodejs/met_http_createserver.asp

const http = require('http');

const port = 1245;

const app = http.createServer((request, response) => {
  response.writeHead(200, { 'Content-Type': 'text/plain' });
  response.write('Hello Holberton School!'); // print message
  response.end();
});
app.listen(port, (error) => {
  if (error) {
    console.log('Something went wrong', error);
  } else {
    console.log(`Server is listening on port ${port}`);
  }
});
module.exports = app;
