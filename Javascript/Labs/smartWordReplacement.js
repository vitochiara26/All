function myReplace(str, before, after) {
    // Comprueba si el primer carácter de 'before' está en mayúscula
    const isCapitalized = before[0] === before[0].toUpperCase();

    // Ajusta la primera letra de 'after' según el caso de 'before'
    let formattedAfter;
    if (isCapitalized) {
        formattedAfter = after[0].toUpperCase() + after.slice(1);
    } else {
        formattedAfter = after[0].toLowerCase() + after.slice(1);
    }

    // Reemplaza la palabra original con la nueva palabra formateada
    return str.replace(before, formattedAfter);
}

console.log(myReplace("Let us go to the store", "store", "mall"));
console.log(myReplace("He is Sleeping on the couch", "Sleeping", "sitting"));
console.log(myReplace("I think we should look up there", "up", "Down"));
console.log(myReplace("This has a spellngi error", "spellngi", "spelling"));
console.log(myReplace("His name is Tom", "Tom", "john"));
console.log(myReplace("Let us get back to more Coding", "Coding", "algorithms"));