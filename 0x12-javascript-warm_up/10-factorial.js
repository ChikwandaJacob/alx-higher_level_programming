#!/usr/bin/node

function fact (num) {
  if (!isNaN(num)) {
    if (num === 1) {
      return 1;
    } else {
      return num * fact(num - 1);
    }
  } else {
    return 1;
  }
}

// Test Function
const num = parseInt(process.argv[2]);
console.log(fact(num));
