#!/usr/bin/node

const list = process.argv.map(item => parseInt(item)).sort((i, j) => {
  return i - j;
}).slice(2);
const len = list.length;

if (len <= 1) {
  console.log(0);
} else {
  console.log(list[len - 2]);
}
