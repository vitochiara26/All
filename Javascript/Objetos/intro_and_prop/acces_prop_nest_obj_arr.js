const person = {
    name: "Alice",
    age: 30,
    contact: {
        email: "alice@example.com",
        phone: {
            home: "123-456-7890",
            work: "098-765-4321"
        }
    }
};

console.log(person.contact.phone.work); // "098-765-4321"
console.log(person['contact']['phone']['work']); // "098-765-4321"

const person2 = {
    name: "Jackson",
    age: 43,
    addresses: [
        { type: "home", street: "123 Main St", city: "Anytown" },
        { type: "work", street: "456 Market St", city: "Workville" }
    ]
};

console.log(person2.addresses[1].city); // "Workville"
