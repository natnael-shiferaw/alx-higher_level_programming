#!/usr/bin/node

// Import the built-in Node.js 'fs' module.
const fs = require('fs');

// Import the 'request' module.
const request = require('request');

// Perform an HTTP GET request to the specified URL and pipe the response to a file.
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
