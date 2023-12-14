#!/usr/bin/node
const { callMeMoby } = require('./101-call_me_moby');

callMeMoby(3, () => {
  console.log('C is fun');
});
