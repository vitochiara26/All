function destroyer(arr, ...args) {
    const notDestroy = [];
    for (let i = 0; i < arr.length; i++) {
        if (!args.includes(arr[i])) {
            notDestroy.push(arr[i]);
        }
    }
    return notDestroy;
}

console.log(destroyer([1, 2, 3, 1, 2, 3], 2, 3));
console.log(destroyer([1, 2, 3, 5, 1, 2, 3], 2, 3));
console.log(destroyer([3, 5, 1, 2, 2], 2, 3, 5));
console.log(destroyer([2, 3, 2, 3], 2, 3));
console.log(destroyer(["tree", "hamburger", 53], "tree", 53));
console.log(destroyer(["possum", "trollo", 12, "safari", 
    "hotdog", 92, 65, "grandma", "bugati", "trojan", "yacht"],
    "yacht", "possum", "trollo", "safari", "hotdog", "grandma", "bugati", "trojan"));