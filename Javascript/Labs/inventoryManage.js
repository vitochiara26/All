const inventory = [];

function findProductIndex(searchName) {
    for (let i = 0; i < inventory.length; i++) {
        if (searchName.toLowerCase() === inventory[i].name) {
            return i;
        }
    }
    return -1;
}

function addProduct(productObject) {
    productObject.name = productObject.name.toLowerCase();
    const index = findProductIndex(productObject.name)
    if (index >= 0) {
        inventory[index].quantity += productObject.quantity;
        console.log(`${productObject.name} quantity updated`);
    } else {
        inventory.push(productObject);
        console.log(`${productObject.name} added to inventory`);
    }
}

addProduct({ name: "flour", quantity: 4 });
addProduct({ name: "sugar", quantity: 6 });
console.log(inventory)

function removeProduct(productName, removeQuant) {
    productName = productName.toLowerCase();
    const index = findProductIndex(productName)
    if (index >= 0) {
        if (inventory[index].quantity >= removeQuant) {
            inventory[index].quantity -= removeQuant;
            console.log(`Remaining ${inventory[index].name} pieces: ${inventory[index].quantity}`);
            if (inventory[index].quantity <= 0) {
                inventory.splice(index, 1);
            }
        } else {
            console.log(`Not enough ${inventory[index].name} available,
                remaining pieces: ${inventory[index].quantity}`);
        }
    } else {
        console.log(`${productName} not found`);
    }
}

removeProduct("sugar", 6);
console.log(inventory)
