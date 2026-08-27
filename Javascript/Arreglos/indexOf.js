let fruits = ["apple", "banana", "orange", "banana"];
let index = fruits.indexOf("banana");
console.log(index); // 1

index = fruits.indexOf("grape");
console.log(index); // -1

let colors = ["red", "green", "blue", "yellow", "green"];
index = colors.indexOf("green", 3);
console.log(index); // 4
