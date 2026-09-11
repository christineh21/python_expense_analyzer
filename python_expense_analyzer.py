def get_amount():
    while True:
        try:
            amount = float(input("How much did you spend? "))

            if amount < 0:
                print("Amount cannot be negative.")
            else:
                return amount

        except ValueError:
            print("Please enter a valid number.")


def add_expense(expenses):
    amount = get_amount()
    category = input("What is the category? ")
    description = input("What did you buy? ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)

    print("Expense added!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    print("\nYour expenses:")

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. "
            f"{expense['category']} - "
            f"{expense['description']} - "
            f"{expense['amount']:.2f}"
        )


def show_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total spent: {total:.2f}")


def category_summary(expenses):
    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    print("\nSpending by category:")

    for category, amount in categories.items():
        print(f"{category}: {amount:.2f}")


def main():
    expenses = []

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show total")
        print("4. Show category summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            show_total(expenses)

        elif choice == "4":
            category_summary(expenses)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()