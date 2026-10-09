function translatePigLatin(str) {
    // Expresión regular para identificar vocales
    const vowelRegex = /[aeiou]/i;

    // Caso 1: Comienza con vocal
    if (vowelRegex.test(str[0])) {
        return str + "way";
    }

    // Buscar el índice de la primera vocal
    const firstVowelIndex = str.search(vowelRegex);

    // Caso 2: No tiene ninguna vocal
    if (firstVowelIndex === -1) {
        return str + "ay";
    }

    // Caso 3: Comienza con una o más consonantes
    const consonantCluster = str.slice(0, firstVowelIndex);
    const restOfString = str.slice(firstVowelIndex);

    return restOfString + consonantCluster + "ay";
}

console.log(translatePigLatin("california"));
console.log(translatePigLatin("paragraphs"));
console.log(translatePigLatin("glove"));
console.log(translatePigLatin("algorithm"));
console.log(translatePigLatin("eight"));
console.log(translatePigLatin("schwartz"));
console.log(translatePigLatin("rhythm"));