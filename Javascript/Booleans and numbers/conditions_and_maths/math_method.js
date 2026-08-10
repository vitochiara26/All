const randomNum = Math.random();
console.log(randomNum); // any number between 0 and 1 – 0 inclusive and 1 exclusive

const smallest = Math.min(1, 5, 3, 9);
console.log(smallest); // 1

const largest = Math.max(1, 5, 3, 9);
console.log(largest); // 9

console.log(Math.ceil(4.3)); // 5
console.log(Math.floor(4.7)); // 4

console.log(Math.round(2.3)); // 2
console.log(Math.round(4.5)); // 5
console.log(Math.round(4.8)); // 5

const max = 10;
const min = 5;
const randomNumber = Math.floor(Math.random() * (max - min + 1)) + min;
console.log(randomNumber);

const randomNumBtw1And20 = Math.floor(Math.random() * 20) + 1;
console.log(randomNumBtw1And20);

console.log(Math.trunc(2.9)); // 2
console.log(Math.trunc(9.1)); // 9

console.log(Math.sqrt(81)); // 9
console.log(Math.cbrt(27)); // 3

console.log(Math.abs(-5)); // 5
console.log(Math.abs(5)); // 5

console.log(Math.pow(2, 3)); // 8
console.log(Math.pow(8, 2)); // 64