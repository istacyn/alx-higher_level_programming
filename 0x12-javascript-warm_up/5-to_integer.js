#!/usr/bin/node
const arg = process.argv[2];
const myNum = Number(arg);

if (!isNaN(myNum) && Number.isInteger(myNum)) {
  console.log(`My number: ${myNum}`);
} else {
  console.log('Not a number');
}
