#!/usr/bin/node
let x = process.argv[2];
if (isNaN(parseInt(x))) { console.log('Missing number of occurrences'); }

while (x-- && x > -1) { console.log('C is fun'); }
