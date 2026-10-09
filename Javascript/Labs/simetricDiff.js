function diffArray(arr1, arr2) {
    let diffSimArr = [];
    const arr1Filtered = arr1.filter((element) => !arr2.includes(element))
    const arr2Filtered = arr2.filter((element) => !arr1.includes(element))
    diffSimArr = diffSimArr.concat(arr1Filtered, arr2Filtered)
    return diffSimArr;
}

const arrayA = ["diamond", "stick", "apple"];
const arrayB = ["stick", "emerald", "bread"];

console.log(diffArray(arrayA, arrayB));
console.log(diffArray(
    ["diorite", "andesite", "grass", "dirt", "pink wool", "dead shrub"],
    ["diorite", "andesite", "grass", "dirt", "dead shrub"]));
console.log(diffArray(
    ["diorite", "andesite", "grass", "dirt", "pink wool",
        "dead shrub"], ["andesite", "grass", "dirt", "dead shrub"]));
console.log(diffArray(
    ["pen", "book"],
    ["book", "pencil", "notebook"]));
console.log(diffArray(
    ["car", "bike", "bus"],
    ["bike", "train", "plane", "bus"]));
console.log(diffArray(
    ["apple", "orange"],
    ["apple", "orange", "banana", "grape"]));
console.log(diffArray(
    [],
    ["apple", "banana"]));
