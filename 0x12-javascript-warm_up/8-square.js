#!/usr/bin/node
// prints square using char x
// use repeat function and argument x

if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  const size = parseInt(process.argv[2]);
  for (let i = 0; i < size; i++) { console.log('X'.repeat(size));
  } }
