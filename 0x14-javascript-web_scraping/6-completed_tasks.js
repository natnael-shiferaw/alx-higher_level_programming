#!/usr/bin/node

const request = require('request');

// Retrieve the API URL from command-line arguments.
const apiUrl = process.argv[2];

// Perform an HTTP GET request to the specified API URL.
request(apiUrl, function (error, response, body) {
  // Check for errors and successful response status code.
  if (!error && response.statusCode === 200) {
    try {
      // Parse the JSON response body.
      const todos = JSON.parse(body);

      // Initialize an object to store completed todo counts by user ID.
      const completed = {};

      // Iterate through todos and count completed todos for each user.
      todos.forEach((todo) => {
        if (todo.completed) {
          completed[todo.userId] = (completed[todo.userId] || 0) + 1;
        }
      });

      // Generate output with completed todo counts.
      const output = `{${Object.entries(completed).map(([key, value]) => ` '${key}': ${value}`).join(',\n ')} }`;

      // Print output if more than 2 users have completed todos, otherwise print the completed object.
      console.log(Object.keys(completed).length > 2 ? output : completed);
    } catch (parseError) {
      // Log an error if there's an issue parsing JSON.
      console.error('Error parsing JSON:', parseError);
    }
  } else {
    // Log an error if there's an HTTP error or non-200 status code.
    console.error('Error:', error);
  }
});
