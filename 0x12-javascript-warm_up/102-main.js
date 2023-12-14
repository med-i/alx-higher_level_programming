#!/usr/bin/node
const { addMeMaybe } = require('./102-add_me_maybe');

addMeMaybe(4, (nb) => {
  console.log(`New value: ${nb}`);
});
