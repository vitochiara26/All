const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map((num) => num * 2);
console.log(numbers); // [1, 2, 3, 4, 5]
console.log(doubled); // [2, 4, 6, 8, 10]

const numbers2 = [3, 4, 5, 6, 7].map((element) => {
    console.log("Element:", element);
    return element * 2;
});

const numbers3 = [3, 4, 5, 6, 7].map((element, index) => {
    console.log("Element:", element);
    console.log("Index:", index);
    return element * 2;
});

const numbers4 = [3, 4, 5, 6, 7].map((element, index, array) => {
    console.log("Element:", element);
    console.log("Index:", index);
    console.log("Array:", array);
    return element * 2;
});