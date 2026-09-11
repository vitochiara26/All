function titleCase(sentence) {
    const words = sentence.split(" ");
    for (let i = 0; i < words.length; i++) {
        let word = words[i].toLowerCase().split("");
        word[0] = word[0].toUpperCase();
        word = word.join("");
        words[i] = word;
    }
    return words.join(" ");
}

console.log(titleCase("i like to code"));
console.log(titleCase("javascript is fun"));
console.log(titleCase("I'm a little tea pot"));
console.log(titleCase("sHoRt AnD sToUt"));
console.log(titleCase("HERE IS MY HANDLE HERE IS MY SPOUT"));
