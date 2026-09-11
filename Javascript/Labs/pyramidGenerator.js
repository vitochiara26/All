function pyramid(char, rows, way) {
    const aroundSpace = rows * 2 - 1;
    let round = 0
    let output = "\n";
    if (way) {
        for (let i = aroundSpace; round < rows; i -= 2) {
            round++;
            let row = char.repeat(i);
            let msg = " ".repeat((aroundSpace - row.length) / 2) + row + "\n"
            output += msg;
        }
    } else {
        for (let i = 1; round < rows; i += 2) {
            round++;
            let row = char.repeat(i);
            let msg = " ".repeat((aroundSpace - row.length) / 2) + row + "\n"
            output += msg;
        }
    }
    return output;
}

console.log(pyramid("o", 4, false))
console.log(pyramid("o", 4, true))
