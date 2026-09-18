const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.sort();

console.log(fruits); // ["Apple", "Banana", "Mango", "Orange"] 

const numbers = [414, 200, 5, 10, 3];
numbers.sort();
console.log(numbers); // [10, 200, 3, 414, 5]

const numbers2 = [414, 200, 5, 10, 3];
numbers2.sort((a, b) => a - b);
console.log(numbers2); // [3, 5, 10, 200, 414]

const fruits2 = ["Banana", undefined, "Apple", "Mango"];
fruits2.sort();

console.log(fruits2); // ["Apple", "Banana", "Mango", undefined]