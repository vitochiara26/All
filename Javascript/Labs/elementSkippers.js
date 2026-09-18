function dropElements(arr, func) {
    let newArr = [];
    for (let i = 0; i < arr.length; i++) {
        if (func(arr[i])) {
            newArr = arr.slice(i);
            break;
        }
    }
    return newArr;
}

console.log(dropElements([1, 2, 3, 4], function (n) { return n >= 3; }));

console.log(dropElements([0, 1, 0, 1], function (n) { return n === 1; }));

console.log(dropElements([1, 2, 3], function (n) { return n > 0; }));

console.log(dropElements([1, 2, 3, 4], function (n) { return n > 5; }));

console.log(dropElements([1, 2, 3, 7, 4], function (n) { return n > 3; }));

console.log(dropElements([1, 2, 3, 9, 2], function (n) { return n > 2; }));