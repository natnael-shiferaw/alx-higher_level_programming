#!/usr/bin/node

const fs = require('fs');

// Write data to a file specified as the third command-line argument (process.argv[2]).
fs.writeFile(process.argv[2], process.argv[3], 'utf8', error => {
  if (error) {
    // Log an error message if an error occurs during the write operation
    console.error(error);
  }
});
