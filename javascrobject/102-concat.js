#!/usr/bin/node
const fs = require('fs');
const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];
fs.readFile(file1, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    fs.appendFile(file3, data, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
fs.readFile(file2, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    fs.appendFile(file3, data, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
