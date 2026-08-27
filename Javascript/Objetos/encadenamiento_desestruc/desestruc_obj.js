const person = { name: "Alice", age: 30, city: "New York" };

const { name, age } = person;

console.log(name); // Alice
console.log(age);  // 30

let { name: personName, age: personAge } = person;

console.log(personName); // Alice
console.log(personAge); //  30

let { name2, age2, country = "Unknown" } = person;

console.log(country); // Unknown

const recipe = {
    name: "Chocolate Cake",
    ingredients: {
        flour: "2 cups",
        sugar: "1 cup"
    }
};

// Extract `flour` from `ingredients`
const { ingredients: { flour } } = recipe;

console.log(flour); // "2 cups"

let name3 = "Bob";
let age3 = 25;

let person2 = { name3, age3 };

console.log(person2); // { name: "Bob", age: 25 } 

function createPerson(name, age) {
    return { name, age };
}

let person3 = createPerson("Charlie", 35);
console.log(person3); // { name: "Charlie", age: 35 } 