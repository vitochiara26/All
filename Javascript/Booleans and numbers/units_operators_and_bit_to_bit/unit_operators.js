const str = '42';
const strToNum = +str;

console.log(str); // 42

console.log(strToNum); // 42
console.log(typeof str); // string
console.log(typeof strToNum); // number 

const strToNegativeNum = -str;

console.log(strToNegativeNum); // -42
console.log(typeof str); // string
console.log(typeof strToNegativeNum); // number

let isOnline = true;
console.log(!isOnline); // false

let isOffline = false;
console.log(!isOffline); // true

const num = 5; // The binary for 5 is 00000101

console.log(~num); // -6

const result = void (2 + 2);

console.log(result); // undefined