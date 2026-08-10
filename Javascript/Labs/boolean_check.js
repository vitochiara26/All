function booWho(boolean) {
    if (typeof boolean === "boolean") {
        return true
    }
    return false
}

console.log(booWho(false))