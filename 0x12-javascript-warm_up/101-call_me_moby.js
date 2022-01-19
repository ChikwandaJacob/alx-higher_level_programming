#!/usr/bin/node

module.exports.callMeMoby = (count, callback) => {
  let i = 0;
  while (i < count) {
    callback();
    i++;
  }
};
