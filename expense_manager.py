import csv

expenses = []


def load_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) < 3:
                    continue

                expense = {
                    "description": row[0],
                    "amount": float(row[1]),
                    "category": row[2]
                }

                expenses.append(expense)

    except FileNotFoundError:
        pass


def save_expense(description, amount, category):
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([description, amount, category])


def add_expense(description, amount, category):
    expense = {
        "description": description,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    save_expense(description, amount, category)


def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['description']} | "
            f"${expense['amount']:.2f} | "
            f"{expense['category']}"
        )


def total_expenses():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


def search_by_category(category):
    found = False

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print(
                f"{expense['description']} - "
                f"${expense['amount']:.2f}"
            )
            found = True

    if not found:
        print("No expenses found for this category.")