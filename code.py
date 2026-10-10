expenses = [
    {
        "id": 1,
        "title": "Grocery Shopping",
        "amount": 1250.0,
        "category": "Food & Groceries",
        "date": "2026-10-01",
        "payment_method": "UPI / GPay",
        "note": "Vegetables, milk, and snacks"
    },
    {
        "id": 2,
        "title": "Metro & Bus Card Recharge",
        "amount": 500.0,
        "category": "Transportation",
        "date": "2026-10-01",
        "payment_method": "Debit Card",
        "note": "Monthly commute pass"
    },
    {
        "id": 3,
        "title": "Python Programming Textbook",
        "amount": 650.0,
        "category": "Education",
        "date": "2026-09-28",
        "payment_method": "UPI / GPay",
        "note": "Reference book for college"
    },
    {
        "id": 4,
        "title": "High Speed WiFi Bill",
        "amount": 799.0,
        "category": "Bills & Utilities",
        "date": "2026-09-25",
        "payment_method": "Net Banking",
        "note": "Broadband monthly plan"
    },
    {
        "id": 5,
        "title": "Weekend Movie & Popcorn",
        "amount": 450.0,
        "category": "Entertainment",
        "date": "2026-09-21",
        "payment_method": "Cash",
        "note": "Cinema with friends"
    }
]


def show_expenses():
    print("\n----- ALL EXPENSES -----")

    for expense in expenses:
        print("\nID:", expense["id"])
        print("Title:", expense["title"])
        print("Amount: ₹", expense["amount"])
        print("Category:", expense["category"])
        print("Date:", expense["date"])
        print("Payment:", expense["payment_method"])
        print("Note:", expense["note"])


def total_expenses():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("\nTotal Expenses: ₹", total)


def category_expenses():
    category = input("\nEnter category: ")

    total = 0
    found = False

    print("\n----- CATEGORY EXPENSES -----")

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            found = True

            print("\nID:", expense["id"])
            print("Title:", expense["title"])
            print("Amount: ₹", expense["amount"])
            print("Category:", expense["category"])
            print("Date:", expense["date"])
            print("Payment:", expense["payment_method"])
            print("Note:", expense["note"])

            total += expense["amount"]

    if found:
        print("\nTotal for", category, ": ₹", total)
    else:
        print("\nNo expenses found for", category)


def add_expense():
    new_id = len(expenses) + 1

    title = input("Enter title: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date: ")
    payment = input("Enter payment method: ")
    note = input("Enter note: ")

    new_expense = {
        "id": new_id,
        "title": title,
        "amount": amount,
        "category": category,
        "date": date,
        "payment_method": payment,
        "note": note
    }

    expenses.append(new_expense)

    print("\nExpense added successfully!")


while True:

    print("\n========== EXPENSE TRACKER ==========")
    print("1. Show all expenses")
    print("2. Show total expenses")
    print("3. Show category expenses")
    print("4. Add expense")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        show_expenses()

    elif choice == "2":
        total_expenses()

    elif choice == "3":
        category_expenses()

    elif choice == "4":
        add_expense()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
