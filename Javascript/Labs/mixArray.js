function frankenSplice(arr1, arr2, index) {
    const copy1 = arr1.slice();
    const copy2 = arr2.slice();
    for (let i = 0; i < copy1.length; i++) {
        copy2.splice(index + i, 0, copy1[i]);
    }
    return copy2;
}

console.log(frankenSplice([1,2,3], [4,5], 1));
console.log(frankenSplice([1, 2], ["a", "b"], 1));
console.log(frankenSplice(["claw", "tentacle"], ["head", "shoulders", "knees", "toes"], 2));
console.log(frankenSplice([1, 2, 3, 4], [], 0));
