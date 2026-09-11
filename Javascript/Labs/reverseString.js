function reverseString(word) {
    const strReverse = word.split("").reverse().join("");
    return strReverse;
}

console.log(reverseString("hello"));
console.log(reverseString("Howdy"));
console.log(reverseString("Greetings from Earth"));