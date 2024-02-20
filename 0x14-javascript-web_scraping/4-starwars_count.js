#!/usr/bin/node

// Import the 'request' module.
const request = require('request');

// Perform an HTTP GET request to the specified URL.
request(process.argv[2], function (error, response, body) {
  // Check for errors during the HTTP request.
  if (!error) {
    // Extract the "results" array from the JSON data.
    const results = JSON.parse(body).results;

    // Count the number of movies containing a character with ID 18.
    console.log(results.reduce((count, movie) => {
      // Check if there is a character with ID 18 ('/18/') in the 'characters' array.
      return movie.characters.find((character) => character.endsWith('/18/'))
        // If found, increment the count by 1.
        ? count + 1
        // keep the count unchanged Otherwise.
        : count;
    }, 0));
  }
});
