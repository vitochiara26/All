const num = 42;
const numObj = Object(num); // Creates an object wrapper for the number

console.log(numObj);
console.log(typeof numObj); // "object"

const newObj = new Object(undefined);
console.log(newObj); // {}

function toObject(value) {
    if (value === null || value === undefined) {
        return {};
    }

    if (typeof value === "object") {
        return value;
    }

    return Object(value);
}

console.log(toObject(null));

console.log(toObject(true));

console.log(toObject([1, 2, 3]));
