function sumFibs(limit) {
    let a = 0;
    let b = 1;
    let c = 0;
    let sum = 1;
    while (c < limit) {
        c = a + b;
        if (c % 2 !== 0 && c <= limit) {
            sum += c
        }
        a = b;
        b = c;
    }
    return sum
}

console.log(sumFibs(1));
console.log(sumFibs(1000));
console.log(sumFibs(4000000));
console.log(sumFibs(4));
console.log(sumFibs(75024));
console.log(sumFibs(75025));