
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*") + "\n"

        items = ""
        for entry in self.ledger:
            desc = f"{entry['description'][:23]:23}"
            amt = f"{entry['amount']:>7.2f}"
            items += f"{desc}{amt}\n"

        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    spendings = []
    for cat in categories:
        spent = sum(item["amount"] for item in cat.ledger if item["amount"] < 0)
        spendings.append(abs(spent))

    total_spent = sum(spendings)

    percentages = [(s / total_spent * 100) // 10 * 10 for s in spendings]

    header = "Percentage spent by category\n"
    chart = ""
    for i in range(100, -1, -10):
        chart += f"{str(i).rjust(3)}| "
        for pct in percentages:
            chart += "o  " if pct >= i else "   "
        chart += "\n"

    footer_line = "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(cat.name) for cat in categories)
    names_row = ""
    for i in range(max_len):
        names_row += "     "
        for cat in categories:
            if i < len(cat.name):
                names_row += f"{cat.name[i]}  "
            else:
                names_row += "   "
        if i < max_len - 1:
            names_row += "\n"
    return header + chart + footer_line + names_row



food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(25.50)

print(food)
print(create_spend_chart([food, clothing]))
