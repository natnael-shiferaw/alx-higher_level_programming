#!/usr/bin/node

const fs = require('fs');

// Read the contents of a file specified as a command-line argument
// 'utf8' specifies the encoding of the file being read
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  if (error) {
    // Log an error message if an error occurs during the file read operation
    console.error('Error reading the file:', error);
  } else {
    // Log the contents of the file if it is read successfully
    console.log(content);
  }
});
