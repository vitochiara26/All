const fruits = ['apple', 'banana', 'orange'];
console.log(fruits.length); // 3

const sparseArray = [1, , , 4];
console.log(sparseArray.length); // 4

const emptyArray = new Array(5);
console.log(emptyArray.length); // 5
console.log(emptyArray); // [ , , , , ]

const fixedLengthArray = Array.from({ length: 5 });
console.log(fixedLengthArray.length); // 5
console.log(fixedLengthArray); // [undefined, undefined, undefined, undefined, undefined]

const filledArray = new Array(3).fill(0);
console.log(filledArray); // [0, 0, 0]