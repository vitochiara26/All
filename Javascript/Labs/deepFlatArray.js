function steamrollArray(arr) {
    const flattened = [];

    for (let i = 0; i < arr.length; i++) {
        if (Array.isArray(arr[i])) {
            flattened.push(...steamrollArray(arr[i]));
        } else {
            flattened.push(arr[i]);
        }
    }

    return flattened;
}

console.log(steamrollArray([[["a"]], [["b"]]]));
console.log(steamrollArray([1, [2], [3, [[4]]]]));
console.log(steamrollArray([1, [], [3, [[4]]]]));
console.log(steamrollArray([1, {}, [3, [[4]]]]));
