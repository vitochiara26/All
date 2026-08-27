const person = {
    name: "Alice",
    age: 30
};

console.log(person.hasOwnProperty("name")); // true
console.log(person.hasOwnProperty("job")); // false

console.log(Object.hasOwn(person, "name")); // true
console.log(Object.hasOwn(person, "job")); // false

console.log("name" in person);  // true

const user = {
    username: "coder123",
    score: 0,
    isActive: false,
    nickname: null
};

// Object.hasOwn() correctly reports these all exist
console.log(Object.hasOwn(user, "score"));    // true  (value is 0, but property exists)
console.log(Object.hasOwn(user, "isActive")); // true  (value is false, but property exists)
console.log(Object.hasOwn(user, "nickname")); // true  (value is null, but property exists)
console.log(Object.hasOwn(user, "email"));   // false (property was never added)

// Danger! Using if() directly gives wrong results for falsy values
if (user.score) {
    console.log("Has score"); // This will NOT print even though score exists!
}

// Safe! Object.hasOwn() gives correct result
if (Object.hasOwn(user, "score")) {
    console.log("Has score:", user.score); // Has score: 0
}

const car = {
    brand: "Toyota",
    model: "Corolla",
    year: 2020
};

console.log(car.brand !== undefined); // true
console.log(car.color !== undefined); // false