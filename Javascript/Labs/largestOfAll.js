function largestOfAll(array) {
    const outputArray = [];
    for (let i = 0; i < array.length; i++) {
        let largestElement = array[i][0];
        for (let j = 0; j < array[i].length; j++) {
            if (array[i][j] > largestElement) {
                largestElement = array[i][j];
            }
        }
        outputArray.push(largestElement);
    }
    return outputArray;
}

console.log(largestOfAll([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]));

console.log(largestOfAll([[13, 27, 18, 26], [4, 5, 1, 3], [32, 35, 37, 39], [1000, 1001, 857, 1]]));

console.log(largestOfAll([[4, 9, 1, 3],
                        [13, 35, 18, 26],
                        [32, 35, 97, 39],
                        [1000000, 1001, 857, 1]])
);

console.log(largestOfAll([[17, 23, 25, 12],
                        [25, 7, 34, 48],
                        [4, -10, 18, 21],
                        [-72, -3, -17, -10]])
);
