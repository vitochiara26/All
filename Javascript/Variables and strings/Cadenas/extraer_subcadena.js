let message = "Hello, world!";
let greeting = message.slice(0, 5);

console.log(greeting);  // Hello 

let world = message.slice(7);

console.log(world);  // world!

message = "JavaScript is fun!";
let lastWord = message.slice(-4);

console.log(lastWord);  // fun! 

message = "I love JavaScript!";
let language = message.slice(7, 17);

console.log(language);  // JavaScript 