const regexPosit = /free(?=code)/i;
console.log(regexPosit.test("freeCodeCamp")); // true
console.log(regexPosit.test("free code camp")); // false
console.log(
    regexPosit.test("I need someone for free to write code for me")
); // false

const regexNeg = /free(?!code)/i;
console.log(regexNeg.test("freeCodeCamp")); // false
console.log(regexNeg.test("free code camp")); // true
console.log(
    regexNeg.test("I need someone for free to write code for me")
); // true

const regexLookBPosit = /(?<=free)code/i;
console.log(regexLookBPosit.test("freeCodeCamp")); // true
console.log(regexLookBPosit.test("free code camp")); // false
console.log(
    regexLookBPosit.test("I need someone for free to write code for me")
); // false

const regexLookBNeg = /(?<!free)code/i;
console.log(regexLookBNeg.test("freeCodeCamp")); // false
console.log(regexLookBNeg.test("free code camp")); // true
console.log(
    regexLookBNeg.test("I need someone for free to write code for me")
); // true

