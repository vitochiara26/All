if (null) {
    console.log("This will not run.");
}

if ("freeCodeCamp") {
    console.log("This will run.");
}

let age = 22;

if (age >= 18) {
    console.log("You're eligible to vote"); // You're eligible to vote
}

age = 15;

if (age >= 18) {
    console.log("You're eligible to vote");
} else {
    console.log("You're not eligible to vote"); // You're not eligible to vote
}

const score = 87;

if (score >= 90) {
    console.log('You got an A');
} else if (score >= 80) {
    console.log('You got a B'); // You got a B
} else if (score >= 70) {
    console.log('You got a C');
} else {
    console.log('You failed! You need to study more!');
}

const temperature = 20;
const weather = temperature > 25 ? 'sunny' : 'cool';

console.log(`It's a ${weather} day!`);
