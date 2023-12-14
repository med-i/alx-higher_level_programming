#!/usr/bin/node
function fact (number) {
  if (Number.isNaN(number) || number === 1) return 1;
  let current = number;
  return number * fact(--current);
}

const number = parseInt(process.argv[2], 10);
console.log(fact(number));
