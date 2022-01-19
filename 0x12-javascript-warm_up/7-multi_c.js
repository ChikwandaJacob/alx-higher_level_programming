#!/usr/bin/node

if (process.argv[2]) {
  let count = 0;

  while (count < process.argv[2]) {
    console.log('C is fun');
    count++;
  }
} else {
  console.log('Missing number of occurrences');
}
