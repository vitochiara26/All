const regex = /free(code)camp/i;
console.log("freecodecamp".match(regex)); 

const regex2 = /free(code)camp/i;
console.log("freecodecamp".replace(regex2, "paidcodeworld"));

const regex3 = /free(co+de)camp/i;
console.log("freecoooooooodecamp".replace(regex3, "paidcodeworld"));

const regex4 = /free(co+de)camp/i;
console.log("freecoooooooodecamp".replace(regex4, "paid$1world")); // paidcoooooooodeworld

const regex5 = /free(co+de)camp.*free\1camp/i;
console.log(regex5.test("freecooooodecamp is great i love freecooooodecamp")); // true
console.log(regex5.test("freecooooodecamp is great i love freecodecamp")); // false

const regex6 = /free(?<code>co+de)camp.*free\k<code>camp/i;
console.log(regex6.test("freecooooodecamp is freecooooodecamp")); // true

const regex7 = /free(?<code>co+de)camp/i;
console.log("freecooooodecamp".replace(regex7, "paid$<code>camp")); // paidcooooodecamp

const regexNotCapture = /free(?:code|candy)camp/i;