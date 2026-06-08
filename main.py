from expense_manager import (
    add_expense,
    view_expenses,
    total_expenses,
    load_expenses,
    search_by_category,
    delete_expense
)


load_expenses()

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Search by Category")
    print("5. Delete Expense")
    print("6. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        description = input("Description: ")
        amount = float(input("Amount: "))
        category = input("Category: ")

        if amount <= 0:
            print("Amount must be greater than 0.")
        else:
            add_expense(description, amount, category)
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

        print("Goodbye!")

        break

    else:
        print("Invalid option")