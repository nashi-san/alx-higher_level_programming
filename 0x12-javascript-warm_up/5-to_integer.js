#!/usr/bin/node
const firstArg = process.argv[2];
const num = parseInt(firstArg);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
