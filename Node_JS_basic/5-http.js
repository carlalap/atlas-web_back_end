// task5. Create a more complex HTTP server using Node's HTTP module
// Script that creates a small HTTP server using the http module:
// https://www.w3schools.com/nodejs/met_http_createserver.asp
// task5. Create a more complex HTTP server using Node's HTTP module
// Script that creates a small HTTP server using the http module:
// https://www.w3schools.com/nodejs/met_http_createserver.asp
const http = require('http'); // Import the http module
const countStudents = require('./3-read_file_async'); // Import the countStudents function from the 3-read_file_async module

const port = 1245; // Set the port to 1245
const localhost = '127.0.0.1';

const app = http.createServer(async (request, response) => { // Create a new HTTP server
  response.writeHead(200, { 'Content-Type': 'text/plain' }); // Set the response header
  if (request.url === '/') {
    response.write('Hello Holberton School!');
  } else if (request.url === '/students') { // If the request URL is '/students'
    response.write('This is the list of our students\n');
    try { // Try to fetch the list of students asynchronously
      const dataStudents = await countStudents(process.argv[2]);
      response.write(`${dataStudents.join('\n')}`); // Write the list of students to the response and end the response
    } catch (error) {
      response.end(error.message);
    }
  }
  response.end();
});

app.listen(port, localhost, (error) => { // Start the server and listen on the specified port
  if (error) { // If an error occurs while starting the server
    console.log('Something went wrong', error); // Log the error message
  } else { // If the server starts successfully
    console.log(`Server is listening on port ${port}`); // Log a message indicating that the server is listening on the specified port
  }
});
module.exports = app; // Export the app variable
