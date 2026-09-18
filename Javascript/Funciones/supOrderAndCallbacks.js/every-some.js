const numbers = [2, 4, 6, 8, 10];
const hasAllEvenNumbers = numbers.every((num) => num % 2 === 0);

console.log(hasAllEvenNumbers); // true

const numbers2 = [1, 3, 5, 7, 8, 9];
const hasSomeEvenNumbers = numbers2.some((num) => num % 2 === 0);

console.log(hasSomeEvenNumbers); // true

