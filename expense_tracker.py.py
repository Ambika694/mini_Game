print("===== Expense Tracker Menu =====")
print("1. Add Expense")
print("2. View All Expenses")
print("3. View Total Spend")
print("4. Filter by Category")
print(" 5. Delete Expense")
print("6. Update Expense")
expense = []
while True:
    option = input("Enter your choice (1-6)")
    if option == "1":
        name = input("Enter expense name:")
        amount = int(input("Enter amount:"))
        category = input("Enter category (Food/Travel/Shopping/etc): ")

        new_expense = {"name": name, "amount": amount, "category": category}
        expense.append(new_expense)

    elif option == "2":
        if not expense:
            print("No expenses yet")
        else:
            for i, exp in enumerate(expense, start=1):
                print(f"{i}. {exp['name']} - Rs.{exp['amount']} ({exp['category']})")
    elif option == "3":
        if not expense:
            print("No expenses yet")
        else:
            total = sum(exp["amount"] for exp in expense)
            print(f"Total Spend: Rs. {total}")
    elif option == "4":
        if not expense:
            print("No expenses yet")
        else:
            found = False
            filter_category = input("Enter category to filter: ")

            for i, exp in enumerate(expense, start=1):
                if exp["category"].lower() == filter_category.lower():
                    print(
                        f"{i}. {exp['name']} - Rs.{exp['amount']} ({exp['category']})"
                    )
                    found = True

            if not found:
              print("No expenses found in this category.")
    elif option == "5":
        Delete = int(input("Enter expense number to delete: "))
        if not expense:
            print("No expenses yet")
        else:
            
            if 1 <= Delete <= len(expense):
                expense.pop( Delete -1)
                print("✅ Expense deleted successfully!")
            else:
             print("❌ Invalid expense number.")
    elif  option == "6" :
        if not expense:
            print("No expenses yet")
        else:
            update = int(input("Enter expense number to update: "))
            
        if 1 <= update and len(expense):
            new_name = input("Enter new expense name: ")
            new_amount = int(input("Enter new amount: "))
            new_category = input("Enter new category: ")
            
            expense[update - 1]["name"] = new_name
            expense[update - 1]["amount"] = new_amount
            expense[update - 1]["category"] = new_category
            
            print("✅ Expense updated successfully!")
        else:
           print("❌ Invalid expense number.")
             
    elif option == "7":
        print("Goodbye! Thanks for using Expense Tracker.")
        break
           
           
