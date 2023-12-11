#!/usr/bin/node
const args = process.argv.slice(2);
const size = args.length;
let result = '';

if (size === 0) result = 'No arguments';
else if (size === 1) result = 'Argument found';
else result = 'Arguments found';

console.log(result);
