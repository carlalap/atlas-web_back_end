// TASK6. Create a small HTTP server using Express
// create a small HTTP server using Express module:
// It should be assigned to the variable app and this one must be exported
// HTTP server should listen on port 1245
// Displays Hello Holberton School! in the page body for the endpoint /
const express = require('express');

const app = express();
const port = 1245;

app.get('/', (request, response) => response.send('Hello Holberton School!'));

app.listen(port, (error) => { // Start the server and listen on the specified port
  if (error) { // If an error occurs while starting the server
    console.log('Something went wrong', error); // Log the error message
  } else { // If the server starts successfully
    console.log(`Server is listening on port ${port}`); // Log a message indicating that the server is listening on the specified port
  }
});
module.exports = app; // Export the app variable
