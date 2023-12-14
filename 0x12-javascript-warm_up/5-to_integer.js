#!/usr/bin/node
const arg = process.argv[2];
const number = parseInt(arg, 10);

if (Number.isNaN(number)) console.log('Not a number');
else console.log(`My number: ${number}`);
