const result = "  Hello, World!  "
    .trim()
    .toLowerCase()
    .replace("world", "JavaScript");

console.log(result); // "hello, JavaScript!"

const transactions = [
    { amount: 100, type: "credit" },
    { amount: 20, type: "cash" },
    { amount: 150, type: "credit" },
    { amount: 50, type: "cash" },
    { amount: 75, type: "credit" }
];

const totalCreditWithBonus = transactions
    .filter((transaction) => transaction.type === "credit")
    .map((transaction) => transaction.amount * 1.1)
    .reduce((sum, amount) => sum + amount, 0);

console.log(totalCreditWithBonus); // 357.5

const calculator = {
    total: 0,
    add(n) {
        this.total += n;
        return this;
    },
    multiply(n) {
        this.total *= n;
        return this;
    },
    subtract(n) {
        this.total -= n;
        return this;
    },
    getResult() {
        return this.total;
    }
};

const result2 = calculator.add(5).multiply(2).subtract(3).getResult();
console.log(result2); // 7
