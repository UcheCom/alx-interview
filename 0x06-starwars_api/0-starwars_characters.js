#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, function (err, resp, body) {
  if (err === null) {
    const film = JSON.parse(body)
    const characters = film.characters;
    getChars(characters, 0);
  }
});

function getChars (characters, idx) {
  request(characters[idx], function (err, resp, body) {
    if (err === null) {
      const people = JSON.parse(body);
      console.log(people.name);
      if (idx + 1 < characters.length) {
        getChars(characters, idx + 1);
      }
    }
  });
}
