#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const api_URL = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(api_URL, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  function fetchCharacter (index) {
    if (index >= characters.length) return;

    request(characters[index], (err, res, characterBody) => {
      if (err) {
        console.error(err);
        return;
      }
      const characterData = JSON.parse(characterBody);
      console.log(characterData.name);

      fetchCharacter(index + 1);
    });
  }

  fetchCharacter(0);
});
