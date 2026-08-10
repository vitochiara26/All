let result = 5 + '10';

console.log(result); // 510
console.log(typeof result); // string

result = '10' + 5;

console.log(result); // 105
console.log(typeof result); // string

let subtractionResult = '10' - 5;
console.log(subtractionResult); // 5
console.log(typeof subtractionResult); // number

let multiplicationResult = '10' * 2;
console.log(multiplicationResult); // 20
console.log(typeof multiplicationResult); // number

let divisionResult = '20' / 2;
console.log(divisionResult); // 10
console.log(typeof divisionResult); // number

subtractionResult = 'abc' - 5;
console.log(subtractionResult); // NaN
console.log(typeof subtractionResult); // number

multiplicationResult = 'abc' * 2;
console.log(multiplicationResult); // NaN
console.log(typeof multiplicationResult); // number

divisionResult = 'abc' / 2;
console.log(divisionResult); // NaN
console.log(typeof divisionResult); // number

let result1 = true + 1;
console.log(result1); // 2
console.log(typeof result1); // number

let result2 = false + 1;
console.log(result2); // 1
console.log(typeof result2); // number

const result3 = 'Hello' + true;
console.log(result3); // "Hellotrue"
console.log(typeof result3); // string

result1 = null + 5;
console.log(result1); // 5
console.log(typeof result1); // number

result2 = undefined + 5;
console.log(result2); // NaN
console.log(typeof result2); // number