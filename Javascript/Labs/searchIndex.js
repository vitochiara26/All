function getIndexToIns(array, num) {
    const sortedArr = array.sort((a, b) => a - b);
    const index = sortedArr.findIndex(element => element >= num);
    return index === -1 ? sortedArr.length : index;
}

console.log(getIndexToIns([10, 20, 30, 40, 50], 35));
console.log(getIndexToIns([10, 20, 30, 40, 50], 30));
console.log(getIndexToIns([40, 60], 50));
console.log(getIndexToIns([3, 10, 5], 3));
console.log(getIndexToIns([5, 3, 20, 3], 5));
console.log(getIndexToIns([2, 20, 10], 19));
console.log(getIndexToIns([3, 10, 5], 11));
console.log(getIndexToIns([], 5));