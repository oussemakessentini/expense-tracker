from expense_manager import (
    add_expense,
    view_expenses,
    total_expenses,
    load_expenses,
    search_by_category,
    delete_expense,
    summary_by_category,
    monthly_report
)


load_expenses()

def get_valid_amount():
    while True:
        try:
            amount = float(input("Amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                return amount

        except ValueError:
            print("Please enter a valid number.")

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Search by Category")
    print("5. Delete Expense")
    print("6. Summary by Category")
    print("7. Monthly Report")
    print("8. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        date = input("Date (YYYY-MM-DD): ")
        description = input("Description: ")
        amount = get_valid_amount()
        category = input("Category: ")
        add_expense(description, amount, category, date)
        print("Expense added successfully.")

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total = total_expenses()
        print(f"Total Expenses: ${total:.2f}")

    elif choice == "4":
        category = input("Enter category: ")
        search_by_category(category)


    elif choice == "5":

        view_expenses()

        try:

            index = int(input("Enter expense number to delete: "))

            delete_expense(index)

        except ValueError:

            print("Please enter a valid number.")



    elif choice == "6":

        summary_by_category()



    elif choice == "7":

        month = input("Enter month (YYYY-MM): ")

        monthly_report(month)


    elif choice == "8":

        print("Goodbye!")

        break

    else:
        print("Invalid option")