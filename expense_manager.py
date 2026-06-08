import csv

expenses = []

def save_expense(description, amount):
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            description,
            amount
        ])

def load_expenses():

    try:

        with open("expenses.csv", "r") as file:

            reader = csv.reader(file)

            for row in reader:

                expense = {
                    "description": row[0],
                    "amount": float(row[1])
                }

                expenses.append(expense)

    except FileNotFoundError:

        pass


def add_expense(description, amount):
    expense = {
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
    save_expense(description, amount)


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