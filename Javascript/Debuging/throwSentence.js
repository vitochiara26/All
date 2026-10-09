function validateNumber(input) {
    if (typeof input !== "number") {
        throw new TypeError("Expected a number, but received " + typeof input);
    }
    return input * 2;
}

function divide(numerator, denominator) {
    if (denominator === 0) {
        throw new Error("Cannot divide by zero");
    }
    return numerator / denominator;
}