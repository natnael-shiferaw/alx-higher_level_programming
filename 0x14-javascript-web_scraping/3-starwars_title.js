#!/usr/bin/node

// Import the 'request' module.
const request = require('request');

// Construct the URL for the specific Star Wars film.
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

// Perform an HTTP GET request to the constructed URL using the 'request' module.
request(url, function (error, response, body) {
  // Log the title of the film if the request is successful, otherwise log the error.
  console.log(error || JSON.parse(body).title);
});
