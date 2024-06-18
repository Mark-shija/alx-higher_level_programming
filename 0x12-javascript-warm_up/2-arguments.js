#!/usr/bin/node
// prints message based on number of args passed

const argsPassed = process.argv.slice(2);

if(argsPassed.length === 0)
{
	console.log('No argument');
}
else if(argsPassed.length === 1)
{
	console.log('Argument found');
}
else{
	console.log('Arguments found');
}
