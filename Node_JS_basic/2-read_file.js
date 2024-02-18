// task2. Reading a file synchronously from a CSV DB with Node JS

const fs = require('fs');

const countStudents = (path) => {
  let data;
  const fields = {};

  try {
    data = fs.readFileSync(path);
  } catch (error) {
    // If the database is not available, throw an error
    throw new Error('Cannot load the database');
  }
  // converts the data read from the file into a string and splits the string
  data = data.toString().split('\n');
  // removes any empty lines from the data array
  data = data.filter((item) => item.length > 0);
  //  removes the header row of the CSV file
  data.shift();

  // loop that iterate over each line in the data array.
  data.forEach((item) => {
    if (item.length > 0) {
      const dataRow = item.split(',');
      if (dataRow[3] in fields) {
        fields[dataRow[3]].push(dataRow[0]);
      } else {
        fields[dataRow[3]] = [dataRow[0]];
      }
    }
  });
  // prints the total number of students
  console.log(`Number of students: ${data.length}`);
  // loop taht iterate over each key in the fields object, Each field (CS, SWE)
  for (const field in fields) {
    // checks if the field is not empty
    if (field) {
      const list = fields[field];
      console.log(`Number of students in ${field}: ${list.length}. List: ${list.toString().replace(/,/g, ', ')}`);
    }
  }
};
// exports the countStudent function
module.exports = countStudents;
