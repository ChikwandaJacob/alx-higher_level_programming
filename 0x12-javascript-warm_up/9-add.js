#!/usr/bin/node

function add (a, b) {
  if (a && b) {
    console.log(parseInt(a) + parseInt(b));
  } else {
    console.log('NaN');
  }
}

// Test Function
add(process.argv[2], process.argv[3]);
