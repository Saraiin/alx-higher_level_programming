#!/usr/bin/node
function factorial (num) {
  if (isNaN(num) || num === 0) return 1;
  return num * factorial(n - 1);
}

console.log(factorial(Number(process.argv[2])));
