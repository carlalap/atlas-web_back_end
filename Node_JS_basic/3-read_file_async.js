// task3. Reading a file asynchronously with Node JS
//
const fs = require('fs');

const countStudents = (path) => new Promise((resolve, reject) => {
  fs.readFile(path, 'utf8', (err, fileData) => {
    if (err) {
      reject(new Error('Cannot load the database'));
      return;
    }

    if (fileData) {
      const fields = {};
      // converts the data read from the file into a string and splits the string
      let data = fileData.toString().split('\n');
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
    }
    resolve();
  });
});
// exports the countStudent function
module.exports = countStudents;
