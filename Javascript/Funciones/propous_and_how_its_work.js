function greet() {
    console.log("Hello, Jessica!");
}

greet(); // "Hello, Jessica!"

function greet(name) {
    console.log("Hello, " + name + "!");
}

greet("Alice"); // Hello, Alice!
greet("Nick"); // Hello, Nick!

function doSomething() {
    console.log("Doing something...");
}

let result = doSomething();
console.log(result); // undefined

function calculateSum(num1, num2) {
    return num1 + num2;
}

console.log(calculateSum(3, 4)); // 7

const sum = function (num1, num2) {
    return num1 + num2;
};

console.log(sum(3, 4)); // 7

function greetings(name = "Guest") {
    console.log("Hello, " + name + "!");
}

greetings(); // Hello, Guest!
greetings("Anna"); // Hello, Anna!

