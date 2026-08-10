let phrase = "JavaScript is awesome!";
let result = phrase.includes("awesome");

console.log(result);  // true

phrase = "JavaScript is awesome!";
result = phrase.includes("Awesome");

console.log(result);  // false 

let text = "Hello, JavaScript world!";
result = text.includes("JavaScript", 7);

console.log(result);  // true

result = text.includes("Hello", 7);

console.log(result);  // false 