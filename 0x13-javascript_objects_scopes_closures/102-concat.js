#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const fileAContent = fs.readFileSync(fileA, 'utf8');
const fileBContent = fs.readFileSync(fileB, 'utf8');
const concatenatedContent = fileAContent + fileBContent;

fs.writeFileSync(fileC, concatenatedContent, 'utf8');
