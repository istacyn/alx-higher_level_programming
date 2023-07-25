#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = "18";
let count = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characterData = JSON.parse(body);
    characterData.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(characterId)) {
	  count += 1;
	}
      });
    });
    console.log(count);
  }
});
