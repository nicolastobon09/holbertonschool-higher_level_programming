#!/usr/bin/node
const process = require('process');

const value = process.argv.length;

console.log(value >= 3 ? 'Argument found' : 'No argument');
