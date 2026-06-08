expenses = []


def add_expense(description, amount):
    expense = {
        "description": description,
        "amount": amount
    }

    expenses.append(expense)


def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    for expense in expenses:
        print(f"{expense['description']} - ${expense['amount']:.2f}")


def total_expenses():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total