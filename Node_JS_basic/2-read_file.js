// task2. Reading a file synchronously from a CSV DB with Node JS

const fs = require('fs');

function countStudents(path) {
    try {
        // Read the database file synchronously
        const data = fs.readFileSync(path, 'utf8');
    
        // Parse the data into an array of objects
        const students = data.split('\n').map((line) => {
          const [firstName, lastName, age, field] = line.split(',');
          return { firstName, lastName, age, field };
        });
        // Count the number of students in each field
        const fields = {};
        students.forEach((students) => {
            if (!fields[students.field]) {
                fields[students.field] = [];
            }
            fields[students.field].push(students.firstName);
        });
        // Log the number of students in each field
        Object.keys(fields).forEach((field) => {
        const count = fields[field].length;
        console.log(`Number of students in ${field}: ${count}. List: ${fields[field].join(', ')}`);
        });
        // Log the total number of students
        const total = students.length;
        console.log(`Number of students: ${total}`);
    } catch (error) {
        // If the database is not available, throw an error
        throw new Error('Cannot load the database');
    }
}
module.exports = countStudents;
