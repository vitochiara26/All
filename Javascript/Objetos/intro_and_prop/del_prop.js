const person = {
    name: "Alice",
    age: 30,
    job: "Engineer"
};

delete person.job;

console.log(person.job); // undefined

const person = {
    name: "Bob",
    age: 25,
    job: "Designer",
    city: "New York"
};

const { job, city, ...remainingProperties } = person;

// { name: "Bob", age: 25 }
console.log(remainingProperties);