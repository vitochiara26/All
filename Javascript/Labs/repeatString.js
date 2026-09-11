function repeatStringNumTimes(str, num) {
    let msg = "";
    if (num <= 0) {
        return msg;
    }
    for (let i = 0; i < num; i++) {
        msg += str;
    }
    return msg;
}

console.log(repeatStringNumTimes("*", 3));
console.log(repeatStringNumTimes("abc", 3));
console.log(repeatStringNumTimes("abc", 4));
console.log(repeatStringNumTimes("abc", 1));
console.log(repeatStringNumTimes("*", 8));
console.log(repeatStringNumTimes("abc", -2));
console.log(repeatStringNumTimes("abc", 0));
