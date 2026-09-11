function findLongestWordLength(sentence) {
    const words = sentence.split(" ")
    let longestLength = 0;
    for (const word of words) {
        if (word.trim().length > longestLength) {
            longestLength = word.trim().length;
        }
    }
    return longestLength;
}

console.log(findLongestWordLength("The quick brown fox jumped over the lazy dog"))
console.log(findLongestWordLength("May the force be with you"))
console.log(findLongestWordLength("Google do a barrel roll"))
console.log(findLongestWordLength("Googling do a barrel roll"))
console.log(findLongestWordLength("What is the average airspeed velocity of an unladen swallow"))
console.log(findLongestWordLength("What if we try a super-long word such as otorhinolaryngology"))
