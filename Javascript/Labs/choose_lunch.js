const lunches = [];

function addLunchToEnd(array, string) {
    array.push(string);
    console.log(`${string} added to the end of the lunch menu.`);
    return array;
}

function addLunchToStart(array, string) {
    array.unshift(string);
    console.log(`${string} added to the start of the lunch menu.`);
    return array;
}

function removeLastLunch(array) {
    if (array.length === 0) {
        console.log("No lunches to remove.");
    } else {
        const string = array.pop();
        console.log(`${string} removed from the end of the lunch menu.`);
        return array;
    }
}

function removeFirstLunch(array) {
    if (array.length === 0) {
        console.log("No lunches to remove.");
    } else {
        const string = array.shift();
        console.log(`${string} removed from the start of the lunch menu.`);
        return array;
    }
}

function getRandomLunch(array) {
    if (array.length === 0) {
        console.log("No lunches available.");
    } else {
        const randomIndex = Math.floor(Math.random() * array.length)
        const randomLunch = array[randomIndex]
        console.log(`Randomly selected lunch: ${randomLunch}`);
    }
}

function showLunchMenu(array) {
    if (array.length === 0) {
        console.log("The menu is empty.");
    } else {
        console.log(`Menu items: ${array.join(", ")}`);
    }
}

showLunchMenu(["Greens", "Corns", "Beans"])
showLunchMenu(["Pizza", "Burger", "Fries", "Salad"])