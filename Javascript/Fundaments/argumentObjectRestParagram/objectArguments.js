// function definition
function getSum(num1, num2) {
    return num1 + num2;
}
// function call with extra argument
console.log(getSum(3, 4, 5)); // 7

function logArgs() {
    for (const arg of arguments) {
        console.log(arg);
    }
}

logArgs(1, 2, 3);
// result:
// 1
// 2
// 3

logArgs("example"); // "example"

function getArg() {
    return arguments[1];
}

console.log(getArg(2, 4, 6)); // 4

function getArgs() {
    return arguments.length;
}

console.log(getArgs("Example")); // 1
console.log(getArgs("Another", "Example")); // 2

function hasCat() {
    return [...arguments].includes("cat");
}

console.log(hasCat("dog", "chicken", "cat")); // true
console.log(hasCat("dog", "chicken", "horse")); // false

