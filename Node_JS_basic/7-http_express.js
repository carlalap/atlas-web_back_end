// TASK7.  Create a more complex HTTP server using Express
// create a small HTTP server using Express module:
// It should be assigned to the variable app and this one must be exported
// HTTP server should listen on port 1245
// Displays Hello Holberton School! in the page body for the endpoint /
const express = require('express');
const fs = require('fs');

const countStudents = async (path) => {
  try {
    const DataBase = await fs.promises.readFile(path, { encoding: 'utf8' });
    // store information about the students.
    const fields = {};
    // store the final result
    const dataShow = {};
    let data = DataBase.toString().split('\n');
    data = data.filter((item) => item.length > 0);

    data.shift();
    data.forEach((item) => {
      if (item.length > 0) {
        const row = item.split(',');
        if (row[3] in fields) {
          fields[row[3]].push(row[0]);
        } else {
          fields[row[3]] = [row[0]];
        }
      }
    });
    // creates a property called numberStudents on the dataShow with the # students
    dataShow.numberStudents = `Number of students: ${data.length}`;
    // creates an empty array called studentsFields on the dataShow object.
    dataShow.studentsFields = [];
    for (const field in fields) {
      if (field) {
        const list = fields[field];
        dataShow.studentsFields.push(`Number of students in ${field}: ${list.length}. List: ${list.toString().replace(/,/g, ', ')}`);
      }
    }
    return dataShow;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};

const app = express();
const port = 1245;

app.get('/', (request, response) => {
  response.send('Hello Holberton School!');
});

app.get('/students', (request, response) => {
  response.write('This is the list of our students\n');
  countStudents(process.argv[2]).then((dataShow) => {
    response.write([dataShow.numberStudents].concat(dataShow.studentsFields).join('\n'));
    response.end('\n');
  }).catch((error) => {
    response.end(error.message);
  });
});

app.listen(port, (error) => { // Start the server and listen on the specified port
    if (error) { // If an error occurs while starting the server
      console.log('Something went wrong', error); // Log the error message
    } else { // If the server starts successfully
      console.log(`Server is listening on port ${port}`); // Log a message indicating that the server is listening on the specified port
    }
});
module.exports = app; // Export the app variable
