// 
const fs = require('fs')

const readDatabase = (filePath) => {
    return new Promise((resolve, reject) => {
      fs.promises.readFile(filePath, 'utf8')
        .then((fileData) => {
          const lines = fileData.trim().split('\n');
          const fields = {};
  
          for (const line of lines) {
            const [firstName, , , field] = line.split(',');
            if (!firstName || !field) continue;
  
            if (!fields[field]) {
              fields[field] = [];
            }
            fields[field].push(firstName);
          }
  
          resolve(fields);
        })
        .catch((error) => {
          reject(error);
        });
    });
  };