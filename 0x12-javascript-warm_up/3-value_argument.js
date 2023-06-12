#!/usr/bin/node
const argument = process.argv.slice(2);

if (argument[0]) {
  console.log(argument[0]);
} else {
  console.log('No argument');
}
