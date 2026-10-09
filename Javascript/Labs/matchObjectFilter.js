function whatIsInAName(arr, srcObj) {
    const matchObjects = [];

    for (let i = 0; i < arr.length; i++) {
        let isMatch = true;

        for (const prop in srcObj) {
            if (!arr[i].hasOwnProperty(prop) || arr[i][prop] !== srcObj[prop]) {
                isMatch = false;
            } 
        }

        if (isMatch) {
            matchObjects.push(arr[i]);
        }

    }

    return matchObjects;
}

console.log(whatIsInAName(
    [
        { first: "Romeo", last: "Montague" },
        { first: "Mercutio", last: null },
        { first: "Tybalt", last: "Capulet" }
    ],
    { last: "Capulet" }
)
);

console.log(whatIsInAName(
    [
        { "apple": 1, "bat": 2 },
        { "bat": 2 },
        { "apple": 1, "bat": 2, "cookie": 2 }
    ],
    { "apple": 1, "bat": 2 }
)
);
