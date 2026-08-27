//primitivos: number, bigint, string, boolean, null, undefined, and symbol.
let num1 = 5;
let num2 = num1;
num1 = 10;

console.log(num2); // 5

//no primitivos 
const originalPerson = { name: "John", age: 30 };
const copiedPerson = originalPerson;

originalPerson.age = 31;

console.log(copiedPerson.age); // 31