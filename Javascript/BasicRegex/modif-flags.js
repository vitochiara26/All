const regex = /freeCodeCamp/i;

console.log(regex.test("freeCodeCamp")); // true
console.log(regex.test("freeCodeCamp is great")); // true
console.log(regex.test("I love freeCodeCamp")); // true
console.log(regex.test("freecodecamp")); // true
console.log(regex.test("FREECODECAMP")); // true
console.log(regex.test("free")); // false
console.log(regex.test("code")); // false
console.log(regex.test("camp")); // false

console.log(regex.test("dO yOu LoVe fReEcOdEcAmP?")); // true

const regexp = /freeCodeCamp/gi;

console.log(regexp.test("freeCodeCamp")); // true
console.log(regexp.test("freeCodeCamp is great")); // false
console.log(regexp.test("I love freeCodeCamp")); // true
console.log(regexp.test("freecodecamp")); // false
console.log(regexp.test("FREECODECAMP")); // true
console.log(regexp.test("free")); // false
console.log(regexp.test("code")); // false
console.log(regexp.test("camp")); // false

console.log(regexp.test("freeCodeCamp")); // true
console.log(regexp.test("I loooooooove freeCodeCamp")); // true

console.log(regexp.lastIndex); // 0
console.log(regexp.test("freeCodeCamp")); // true
console.log(regexp.lastIndex); // 12
console.log(regexp.test("freeCodeCamp is great")); // false
console.log(regexp.lastIndex); // 0
console.log(regexp.test("I love freeCodeCamp")); // true
console.log(regexp.lastIndex); // 19
console.log(regexp.test("freecodecamp")); // false
console.log(regexp.lastIndex); // 0
console.log(regexp.test("FREECODECAMP")); // true
console.log(regexp.lastIndex); // 12
console.log(regexp.test("free")); // false
console.log(regexp.lastIndex); // 0
console.log(regexp.test("code")); // false
console.log(regexp.lastIndex); // 0
console.log(regexp.test("camp")); // false

const regex2 = new RegExp("freeCodeCamp", "gi");

console.log(regex2.test("freeCodeCamp")); // true
console.log(regex2.test("FREECODECAMP")); // false

const start = /^freecodecamp/i;
const end = /freecodecamp$/i;
console.log(start.test("freecodecamp")); // true
console.log(end.test("freecodecamp")); // true
console.log(start.test("freecodecamp is great")); // true
console.log(end.test("freecodecamp is great")); // false
console.log(start.test("i love freecodecamp")); // false
console.log(end.test("i love freecodecamp")); // true
console.log(start.test("have met freecodecamp's founder")); // false
console.log(end.test("have met freecodecamp's founder")); // false

const string = `I really love
freecodecamp
it's my favorite`;
console.log(start.test(string)); // false
console.log(end.test(string)); // false

const startExp = /^freecodecamp/im;
const endExp = /freecodecamp$/im;
const stri = `I really love
freecodecamp
it's my favorite`;
console.log(startExp.test(stri)); // true
console.log(endExp.test(stri)); // true

const regexD = /freecodecamp/di;
const stringD = "we love freecodecamp isn't freecodecamp great?";
console.log(string.match(regex));

