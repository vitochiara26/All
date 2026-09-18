function pairElement(elements) {
    const bases = [];
    for (let i = 0; i < elements.length; i++) {
        if (elements[i] === "A") {
            bases.push([elements[i], "T"]);
        } else if (elements[i] === "T") {
            bases.push([elements[i], "A"]);
        } else if (elements[i] === "C") {
            bases.push([elements[i], "G"]);
        } else if (elements[i] === "G") {
            bases.push([elements[i], "C"]);
        }
    }
    return bases;
}

console.log(pairElement("ATCG"));
console.log(pairElement("ATCGA"));
console.log(pairElement("TTGAG"));
console.log(pairElement("CTCTA"));
