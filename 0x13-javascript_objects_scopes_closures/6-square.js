#!/usr/bin/node

const Square1 = require('./5-square.js');

class Square extends Square1 {
  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let line = '';
      let j = 0;
      while (j < this.width) {
        line += c;
        j++;
      }

      console.log(line);
    }
  }
}

module.exports = Square;
