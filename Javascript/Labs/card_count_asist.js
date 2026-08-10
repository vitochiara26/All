let count = 0;

function cardCounter(card) {
    if (card >= 1 && card <= 6) {
        ++count;
    } else if (
        card >= 10 ||
        card === "J" ||
        card === "Q" ||
        card === "K" ||
        card === "A") {
        --count
    }

    if (count > 0) {
        return count + " Bet";
    } else {
        return count + " Hold";
    }
}

cardCounter(2);
cardCounter(3);
cardCounter(4);
cardCounter(5);
cardCounter(2);
console.log(cardCounter(6));
count = 0;

cardCounter(7);
cardCounter(8);
console.log(cardCounter(9));
count = 0;

cardCounter(10);
cardCounter("J");
cardCounter("Q");
cardCounter("K");
console.log(cardCounter("A"));
count = 0;

cardCounter(3);
cardCounter(7);
cardCounter("Q");
cardCounter(8);
console.log(cardCounter("A"));
count = 0;

cardCounter(2);
cardCounter("J");
cardCounter(9);
cardCounter(2);
console.log(cardCounter(7));
count = 0;

cardCounter(2);
cardCounter(2);
console.log(cardCounter(10));
count = 0;

cardCounter(3);
cardCounter(2);
cardCounter("A");
cardCounter(10);
console.log(cardCounter("K"));
count = 0;
