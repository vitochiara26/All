function convertCtoF(tempC) {
    const tempF = tempC * (9 / 5) + 32;
    return tempF;
}

console.log(convertCtoF(0));
console.log(convertCtoF(-30));
console.log(convertCtoF(-10));
console.log(convertCtoF(20));
console.log(convertCtoF(30));