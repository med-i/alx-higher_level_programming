#!/usr/bin/node
const fs = require('fs');

const file = process.argv[2];
const string = process.argv[3];

if (!file || !string) {
  console.error(`Error: ${!file ? 'No file path provided' : 'No string provided'}`);
  process.exit(1);
}

fs.writeFile(file, string, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
