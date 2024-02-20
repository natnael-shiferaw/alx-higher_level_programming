#!/usr/bin/node

const request = require('request');

// Import the 'request' module for making HTTP GET requests.
request.get(process.argv[2])

  // Listen for the response event from the HTTP request.
  .on('response', function (response) {
    // Log the HTTP status code of the response.
    console.log(`code: ${response.statusCode}`);
  });
