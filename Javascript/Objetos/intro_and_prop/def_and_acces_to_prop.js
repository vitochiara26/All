// const exampleObject = {
//     propertyName: value,
// }

const person = {
    name: "Alice",
    age: 30,
    city: "New York"
};

console.log(person.name);  // Alice
console.log(person.age);   // 30 

console.log(person["name"]); // Alice
console.log(person["age"]); //  30

const oddObject = {
    "1stProperty": "Hello",
    "property with spaces": "World"
};

console.log(oddObject["1stProperty"]);  // Hello
console.log(oddObject["property with spaces"]);  // World

let propertyName = "city";
console.log(person[propertyName]); // New York
