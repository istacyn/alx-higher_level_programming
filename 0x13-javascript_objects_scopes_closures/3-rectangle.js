#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let line = '';
      let j = 0;
      while (j < this.width) {
        line += 'X';
        j++;
      }

      console.log(line);
    }
  }
}
module.exports = Rectangle;
