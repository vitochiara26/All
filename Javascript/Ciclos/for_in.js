const fruit = {
    name: 'apple',
    color: 'red',
    price: 0.99
};

for (const prop in fruit) {
    console.log(fruit[prop]);
}

const person = {
    name: 'John',
    age: 30,
    address: {
        street: '123 Main St',
        city: 'Anytown',
        state: 'CA'
    }
};

for (const prop in person) {
    console.log(person[prop]);
}

function isObject(obj) {
    return typeof obj === 'object' && !Array.isArray(obj) && obj !== null;
}

for (const prop in person) {
    if (isObject(person[prop])) {
        for (const nestedProp in person[prop]) {
            console.log(person[prop][nestedProp]);
        }
    } else {
        console.log(person[prop]);
    }
}