function fearNotLetter(str) {
    const alphabet = "abcdefghijklmnopqrstuvwxyz";
    let startIndex = alphabet.indexOf(str[0]);
    let strLong = str.length;
    while (strLong - 1 >= 0) {
        if (!str.includes(alphabet[startIndex + 1])) {
            return alphabet[startIndex + 1];
        }
        strLong -= 1;
        startIndex += 1;
    }
}

console.log(fearNotLetter("abce"));
console.log(fearNotLetter("abcdefghjklmno"));
console.log(fearNotLetter("stvwx"));
console.log(fearNotLetter("bcdf"));
console.log(fearNotLetter("abcdefghijklmnopqrstuvwxyz"));
