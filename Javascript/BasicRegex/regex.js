const regex = /freeCodeCamp/;

const pattern = "freeCodeCamp";
const regEx = new RegExp(pattern);

const test = regex.test("e");
console.log(test);
console.log(regex.test("freeCodeCamp"));
console.log(regex.test("freeCodeCamp is great"));
console.log(regex.test("I love freeCodeCamp"));
console.log(regex.test("freecodecamp"));
console.log(regex.test("FREECODECAMP"));
console.log(regex.test("free"));
console.log(regex.test("code"));
console.log(regex.test("camp"));

const match = "freeCodeCamp".match(regex);
console.log(match);

console.log("freeCodeCamp".match(regex));
// ['freeCodeCamp', index: 0, input: 'freeCodeCamp', groups: undefined]
console.log("freeCodeCamp is great".match(regex));
// ['freeCodeCamp', index: 0, input: 'freeCodeCamp is great', groups: undefined]
console.log("I love freeCodeCamp".match(regex)); 
// ['freeCodeCamp', index: 7, input: 'I love freeCodeCamp', groups: undefined]
console.log("freecodecamp".match(regex)); // null
console.log("FREECODECAMP".match(regex)); // null
console.log("free".match(regex)); // null

const regexp = /freecodecamp/;
const str = "freecodecamp is rly kewl";
const replaced = str.replace(regexp, "freeCodeCamp");
console.log(replaced);


