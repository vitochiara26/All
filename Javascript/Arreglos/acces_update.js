let fruits = ["apple", "banana", "cherry"];
console.log(fruits[1]); // "banana"

fruits = ["apple", "banana", "cherry"];
console.log(fruits[3]); // undefined

fruits = ["apple", "banana", "cherry"];
fruits[1] = "blueberry";
console.log(fruits); // ["apple", "blueberry", "cherry"]

fruits = ["apple", "banana", "cherry"];
fruits[3] = "date";
console.log(fruits); // ["apple", "banana", "cherry", "date"]