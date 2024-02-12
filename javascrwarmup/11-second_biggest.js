#!/usr/bin/node
let args = process.argv.slice(2);
args = args.map(arg => parseInt(arg));
args.sort((a, b) => b - a);
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  console.log(args[1]);
}
