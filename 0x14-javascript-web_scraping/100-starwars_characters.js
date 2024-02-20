#!/usr/bin/node

const request = require('request');

// Retrieve movie ID from command-line arguments.
const movieId = process.argv[2];

// Construct the API URL for the specified movie.
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Perform an HTTP GET request to the movie API URL.
request(apiUrl, function (error, response, body) {
  // Check for successful response and no errors.
  if (!error && response.statusCode === 200) {
    // Parse the JSON response body.
    const movieData = JSON.parse(body);

    // Print movie title.
    console.log(`Characters of "${movieData.title}":`);

    // Iterate through character URLs and fetch character data.
    movieData.characters.forEach((characterUrl) => {
      // Perform an HTTP GET request to the character URL.
      request(characterUrl, function (charError, charResponse, charBody) {
        // Check for successful response and no errors.
        if (!charError && charResponse.statusCode === 200) {
          // Parse the JSON character data.
          const characterData = JSON.parse(charBody);

          // Print character name.
          console.log(characterData.name);
        } else {
          // Log an error if there's an issue fetching character data.
          console.error('Error fetching character data:', charError);
        }
      });
    });
  } else {
    // Log an error if there's an issue fetching movie data.
    console.error('Error fetching movie data:', error);
  }
});
