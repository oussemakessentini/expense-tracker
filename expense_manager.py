import csv
from expense import Expense

expenses = []


def load_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) < 4:
                    continue

                expense = Expense(
                    row[0],
                    float(row[1]),
                    row[2],
                    row[3]
                )

                expenses.append(expense)

    except FileNotFoundError:
        pass


def save_expense(expense):
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(expense.to_list())


def save_all_expenses():
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)

        for expense in expenses:
            writer.writerow(expense.to_list())


def add_expense(description, amount, category, date):
    expense = Expense(description, amount, category, date)
    expenses.append(expense)
    save_expense(expense)


def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense.description} | "
            f"${expense.amount:.2f} | "
            f"{expense.category} | "
            f"{expense.date}"
        )


def total_expenses():
    total = 0

    for expense in expenses:
        total += expense.amount

    return total


def search_by_category(category):
    found = False

    for expense in expenses:
        if expense.category.lower() == category.lower():
            print(
                f"{expense.date} | {expense.description} - "
                f"${expense.amount:.2f}"
            )
            found = True

    if not found:
        print("No expenses found for this category.")


def delete_expense(index):
    if index < 1 or index > len(expenses):
        print("Invalid expense number.")
        return

    removed_expense = expenses.pop(index - 1)
    save_all_expenses()

    print(f"Deleted: {removed_expense.description}")


def summary_by_category():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    summary = {}

    for expense in expenses:
        if expense.category in summary:
            summary[expense.category] += expense.amount
        else:
            summary[expense.category] = expense.amount

    print("\nSummary by Category:")
    for category, total in summary.items():
        print(f"{category}: ${total:.2f}")


def monthly_report(month):
    total = 0

    for expense in expenses:
        if expense.date.startswith(month):
            print(
                f"{expense.date} | {expense.description} | "
                f"${expense.amount:.2f} | {expense.category}"
            )
            total += expense.amount

    print(f"\nMonthly Total: ${total:.2f}")


def export_monthly_report(month):
    report_file = f"monthly_report_{month}.csv"
    total = 0

    with open(report_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Description", "Amount", "Category"])

        for expense in expenses:
            if expense.date.startswith(month):
                writer.writerow(expense.to_list())
                total += expense.amount

        writer.writerow([])
        writer.writerow(["Total", "", total, ""])

    print(f"Report exported successfully: {report_file}")