/* eslint-disable no-console */
/* eslint-disable no-unused-vars */
const fs = require('fs');

let lines;
let currentIndex;
let index;

function partTwo() {
   readLines();
   currentIndex = 0;
   index = 0;


   let outputs = [];
   let solution;
   while (currentIndex < lines.length) {
      let line = getNextLine();
      let number = Number(line);
      index += number;
      if (outputs.includes(index)) {
         solution = index;
         break;
      } else
         outputs.push(index);
      if (currentIndex == lines.length)
         currentIndex = 0;
   }

   console.log('Part two solution: ' + solution);
}

function partOne() {
   readLines();
   currentIndex = 0;
   index = 0;

   while (currentIndex < lines.length) {
      let line = getNextLine();
      let number = Number(line);
      index += number;
   }

   console.log('Part one solution: ' + index);
}

function getNextLine() {
   return lines[currentIndex++];
}

function readLines() {
   let input = fs.readFileSync('../input.txt');
   lines = input.toString().split('\r\n');
}

partOne();
partTwo();