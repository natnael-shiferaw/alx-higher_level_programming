#!/usr/bin/node

const request = require('request');

// Retrieve the movie ID from command-line arguments.
const movieId = process.argv[2];

// Construct the API URL for the specified movie.
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Perform an HTTP GET request to the Star Wars API URL.
request(apiUrl, function (error, response, body) {
  // Check for successful HTTP request.
  if (!error && response.statusCode === 200) {
    // Parse the JSON response body.
    const movieData = JSON.parse(body);

    // Create an array of promises that fetch the data for each individual character.
    const characterPromises = movieData.characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        // Use another 'request' to fetch the data for the individual character.
        request(characterUrl, function (charError, charResponse, charBody) {
          // Check for successful HTTP request for character data.
          if (!charError && charResponse.statusCode === 200) {
            // Parse the JSON character data.
            const characterData = JSON.parse(charBody);
            // Resolve the promise with the name of the character.
            resolve(characterData.name);
          } else {
            // Reject the promise with the error message if there was an error during the HTTP request.
            reject(new Error(`Error fetching character data: ${charError}`));
          }
        });
      });
    });

    // Wait for all character promises to resolve.
    Promise.all(characterPromises)
      .then((characterNames) => {
        // Print the names of all characters.
        console.log(characterNames.join('\n'));
      })
      .catch((error) => {
        // Log any errors encountered during promise execution.
        console.error(error.message);
      });
  } else {
    // Log an error if there was an issue fetching movie data.
    console.error('Error fetching movie data:', error);
  }
});
