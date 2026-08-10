let str = "hello";
let charArray = str.split("");
console.log(charArray); // ["h", "e", "l", "l", "o"]

charArray.reverse();
console.log(charArray); // ["o", "l", "l", "e", "h"]

let reversedString = charArray.join("");
console.log(reversedString); // "olleh"
