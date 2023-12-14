#!/usr/bin/node
const nums = process.argv.slice(2);
let firstMax = Number.MIN_SAFE_INTEGER;
let secondMax = Number.MIN_SAFE_INTEGER;

if (nums.length < 2) {
  secondMax = 0;
} else {
  for (let i = 0; i < nums.length; i++) {
    const num = parseInt(nums[i], 10);

    if (num > firstMax) {
      secondMax = firstMax;
      firstMax = num;
    } else if (num > secondMax) {
      secondMax = num;
    }
  }
}

console.log(secondMax);
