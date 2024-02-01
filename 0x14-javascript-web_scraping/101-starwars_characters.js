#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  } else {
    console.error('Failed to retrieve movie data:', error);
  }
});

function printCharacters (characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], (error, response, body) => {
    if (!error && response.statusCode === 200) {
      console.log(JSON.parse(body).name);
      printCharacters(characters, index + 1);
    } else {
      console.error('Failed to retrieve character data:', error);
    }
  });
}
