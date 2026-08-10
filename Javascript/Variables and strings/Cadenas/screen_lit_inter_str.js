const name = 'Alice'
const greeting = `Hello ${name}!`;

console.log(greeting);

const age = 25;
const message1 = "My name is " + name + " and I am " + age + " years old.";
console.log(message1); 


const message2 = `My name is ${name} and I am ${age} years old.`;
console.log(message2); 

let poem = `Roses are red,
Violets are blue,
JavaScript is fun,
And so are you.`;

console.log(poem);

const song = "Bohemian Rhapsody";
const score = 9.5;
const highestScore = 10;
const output = `One of my favorite songs is "${song}". I rated it ${
  (score / highestScore) * 100
}%.`;
console.log(output); 