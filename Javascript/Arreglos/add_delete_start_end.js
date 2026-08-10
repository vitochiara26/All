const fruits = ["apple", "banana"];
let newLength = fruits.push("orange");
console.log(newLength); // 3
console.log(fruits); // ["apple", "banana", "orange"]

let lastFruit = fruits.pop();
console.log(fruits); // ["apple", "banana"]
console.log(lastFruit); // "orange"

let numbers = [2, 3];
newLength = numbers.unshift(1);
console.log(numbers); // [1, 2, 3]
console.log(newLength); // 3

let colors = ["red", "green", "blue"];
let firstColor = colors.shift();
console.log(colors); // ["green", "blue"]
console.log(firstColor); // "red"