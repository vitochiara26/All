let x = 5;

console.log(++x); // 6
console.log(x); // 6

let y = 5;

console.log(y++); // 5
console.log(y); // 6 

x = 5;
console.log(--x); // 4
console.log(x); // 4

y = 5;
console.log(y--); // 5
console.log(y); // 4

let a = 5;
let b = ++a;
console.log(b); // 6 (a was incremented before assignment)

let c = 5;
let d = c++;
console.log(d); // 5 (c was incremented after assignment) 