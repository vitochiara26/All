//const regex = /^\d\d\d\d$/;
const regex = /^\d{4}$/;
console.log(regex.test("123")); // false
console.log(regex.test("1234")); // true
console.log(regex.test("12345")); // false
console.log(regex.test("123456")); // false
console.log(regex.test("1234567")); // false

const regexMin = /^\d{4,}$/;
console.log(regexMin.test("123")); // false
console.log(regexMin.test("1234")); // true
console.log(regexMin.test("12345")); // true
console.log(regexMin.test("123456")); // true
console.log(regexMin.test("1234567")); // true

const regexMinMax = /^\d{4,6}$/;
console.log(regexMinMax.test("123")); // false
console.log(regexMinMax.test("1234")); // true
console.log(regexMinMax.test("12345")); // true
console.log(regexMinMax.test("123456")); // true
console.log(regexMinMax.test("1234567")); // false

const regexOneLetter = /^[a-zA-Z]?\d{4,6}$/;
console.log(regexOneLetter.test("123")); // false
console.log(regexOneLetter.test("a1234")); // true
console.log(regexOneLetter.test("12345")); // true
console.log(regexOneLetter.test("az12345")); // false
console.log(regexOneLetter.test("X123456")); // true
console.log(regexOneLetter.test("1234567")); // false

const regexMultiLetter = /^[a-zA-Z]*\d{4,6}$/;
console.log(regexMultiLetter.test("123")); // false
console.log(regexMultiLetter.test("a1234")); // true
console.log(regexMultiLetter.test("12345")); // true
console.log(regexMultiLetter.test("az12345")); // true
console.log(regexMultiLetter.test("X123456")); // true
console.log(regexMultiLetter.test("1234567")); // false

const regexMinOneLetter = /^[a-zA-Z]+\d{4,6}$/;
console.log(regexMinOneLetter.test("123")); // false
console.log(regexMinOneLetter.test("a1234")); // true
console.log(regexMinOneLetter.test("12345")); // false
console.log(regexMinOneLetter.test("az12345")); // true
console.log(regexMinOneLetter.test("X123456")); // true
console.log(regexMinOneLetter.test("1234567")); // false