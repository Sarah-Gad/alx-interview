#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        return reject(error);
      }
      resolve(JSON.parse(body));
    });
  });
}

async function printCharacters () {
  const data = await makeRequest(url);
  const characters = data.characters;
  for (let i = 0; i < characters.length; i++) {
    const character = characters[i];
    const person = await makeRequest(character);
    console.log(person.name);
  }
}
printCharacters();
