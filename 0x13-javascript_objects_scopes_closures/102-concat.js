#!/usr/bin/node
const fs = require('fs');

function readFile (file) {
  let text = '';

  try {
    text = fs.readFileSync(file);
  } catch (err) {
    console.error(err);
  }

  return text;
}

const args = process.argv.slice(2);
const fileA = readFile(args[0]);
const fileB = readFile(args[1]);

try {
  fs.writeFileSync(args[2], fileA + fileB);
} catch (err) {
  console.error(err);
}
