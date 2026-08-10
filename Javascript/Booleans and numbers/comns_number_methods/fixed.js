let num = 3.14159;
console.log(num.toFixed(2)); // "3.14"

console.log((3.14159).toFixed(3));  // "3.142"
console.log((3.14449).toFixed(3));  // "3.144"
console.log((3.14550).toFixed(3));  // "3.146"

let num = 3.14159;
console.log(num.toFixed()); // "3"

let price = 19.99;
let taxRate = 0.08;
let total = price + (price * taxRate);

console.log("Total: $" + total.toFixed(2)); // "Total: $21.59"