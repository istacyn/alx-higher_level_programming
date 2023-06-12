#!/usr/bin/node
const size = process.argv[2];

if (!isNaN(size) && Number.isInteger(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let j = 0;
    let line = '';

    while (j < size) {
      line += 'X';
      j++;
    }
    console.log(line);
  }
}
