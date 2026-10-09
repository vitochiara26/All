const regex = /freecodecamp/g;
const str = "freecodecamp is the best we love freecodecamp";
const matched = str.match(regex);
const replaced = str.replace(regex, "freeCodeCamp");
console.log(matched);
console.log(replaced);

const pattern = "freecodecamp";
const strall = "freecodecamp is the best we love freecodecamp";
const matchedall = strall.matchAll(pattern);
const replacedall = strall.replaceAll(pattern, "freeCodeCamp");
console.log(matchedall);
console.log(replacedall);
console.log(matchedall.next());
console.log(matchedall.next());
console.log(matchedall.next());

const matchedal = strall.matchAll(pattern);
console.log(Array.from(matchedal));

