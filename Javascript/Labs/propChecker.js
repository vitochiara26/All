function truthCheck(collection, pre) {
    let isTruth = true;
    for (let i = 0; i < collection.length; i++) {
        if (!collection[i][pre]) {
            isTruth = false;
            break;
        } 
    }
    return isTruth;
}

console.log(truthCheck(
    [
        {
            name: "Quincy",
            role: "Founder",
            isBot: false
        }, {
            name: "Naomi",
            role: "",
            isBot: false
        }, {
            name: "Camperbot",
            role: "Bot",
            isBot: true
        }
    ],
    "isBot"
));

console.log(truthCheck(
    [
        {
            name: "Quincy",
            role: "Founder",
            isBot: false
        }, {
            name: "Naomi",
            role: "",
            isBot: false
        }, {
            name: "Camperbot",
            role: "Bot",
            isBot: true
        }
    ],
    "name"
));

console.log(truthCheck(
    [
        {
            name: "Quincy",
            role: "Founder",
            isBot: false
        }, {
            name: "Naomi",
            role: "",
            isBot: false
        }, {
            name: "Camperbot",
            role: "Bot",
            isBot: true
        }
    ],
    "role"
));

console.log(truthCheck(
    [
        {
            name: "Pikachu",
            number: 25,
            caught: 3
        }, {
            name: "Togepi", 
            number: 175, 
            caught: 1
        }
    ], 
    "number"
));