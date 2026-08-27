const person = {
    name: "Alice",
    age: 30
};

console.log(person.name); // "Alice"
console.log(person.job); // undefined

const user = {
    name: "John",
    profile: {
        email: "john@example.com",
        address: {
            street: "123 Main St",
            city: "Somewhere"
        }
    }
};

console.log(user?.profile?.address?.street); // "123 Main St"
console.log(user?.profile?.phone?.number);   // undefined

