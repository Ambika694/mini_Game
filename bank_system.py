print("╔══════════════════════════════════════╗")
print("║        🏦 BANK MANAGEMENT SYSTEM     ║")
print("╠══════════════════════════════════════╣")
print("║  1. Create Account                   ║")
print("║  2. View All Accounts                ║")
print("║  3. Search Account                   ║")
print("║  4. Deposit Money                    ║")
print("║  5. Withdraw Money                   ║")
print("║  6. Check Balance                    ║")
print("║  7. Delete Account                   ║")
print("║  8. Exit                             ║")
print("╚══════════════════════════════════════╝")

account = []

while True:

    print("\n---------------------------------------")
    option = input("👉 Choose your option: ")
    print("---------------------------------------")

    # ==============================
    # 1. CREATE ACCOUNT
    # ==============================
    if option == "1":

        print("\n========== 📝 CREATE ACCOUNT ==========")

        Name = input("Enter your name: ")
        account_no = int(input("Enter your Account No: "))
        Balance = int(input("Enter your Balance: "))
        age = int(input("Enter your Age: "))

        new_account = {
            "Name": Name,
            "Account_no": account_no,
            "Age": age,
            "Balance": Balance
        }

        account.append(new_account)

        print("---------------------------------------")
        print("✅ Account created successfully!")
        print("---------------------------------------")


    # ==============================
    # 2. VIEW ALL ACCOUNTS
    # ==============================
    elif option == "2":

        print("\n========== 👥 ALL ACCOUNTS ==========")

        if not account:
            print("❌ No accounts yet.")
        else:
            for i, acco in enumerate(account, start=1):

                print(
                    f"{i}. {acco['Name']} | "
                    f"Account No: {acco['Account_no']} | "
                    f"Age: {acco['Age']} | "
                    f"Balance: Rs.{acco['Balance']}"
                )


    # ==============================
    # 3. SEARCH ACCOUNT
    # ==============================
    elif option == "3":

        print("\n========== 🔍 SEARCH ACCOUNT ==========")

        found = False

        if not account:
            print("❌ No accounts yet.")
        else:

            Search_Account = int(
                input("Enter Account number: ")
            )

            for acco in account:

                if Search_Account == acco["Account_no"]:

                    print("\n✅ Account found!")

                    print(f"Name: {acco['Name']}")
                    print(f"Account No: {acco['Account_no']}")
                    print(f"Age: {acco['Age']}")
                    print(f"Balance: Rs.{acco['Balance']}")

                    found = True

            if not found:
                print("❌ Account not found.")


    # ==============================
    # 4. DEPOSIT MONEY
    # ==============================
    elif option == "4":

        print("\n========== 💰 DEPOSIT MONEY ==========")

        found = False

        if not account:
            print("❌ No accounts yet.")

        else:

            Search_Account = int(
                input("Enter Account number: ")
            )

            for acco in account:

                if Search_Account == acco["Account_no"]:

                    print("\n✅ Account found!")

                    Deposit = int(
                        input("Enter deposit amount: ")
                    )

                    acco["Balance"] = (
                        acco["Balance"] + Deposit
                    )

                    print("\n✅ Money deposited successfully!")
                    print(
                        f"New Balance: Rs.{acco['Balance']}"
                    )

                    found = True
                    break

            if not found:
                print("❌ Account not found.")


    # ==============================
    # 5. WITHDRAW MONEY
    # ==============================
    elif option == "5":

        print("\n========== 💸 WITHDRAW MONEY ==========")

        found = False

        if not account:
            print("❌ No accounts yet.")

        else:

            Search_Account = int(
                input("Enter Account number: ")
            )

            for acco in account:

                if Search_Account == acco["Account_no"]:

                    print("\n✅ Account found!")

                    Withdraw = int(
                        input("Enter withdrawal amount: ")
                    )

                    if acco["Balance"] >= Withdraw:

                        acco["Balance"] = (
                            acco["Balance"] - Withdraw
                        )

                        print(
                            "✅ Withdrawal successful!"
                        )

                        print(
                            f"Remaining Balance: "
                            f"Rs.{acco['Balance']}"
                        )

                    else:
                        print("❌ Insufficient balance.")

                    found = True
                    break

            if not found:
                print("❌ Account not found.")


    # ==============================
    # 6. CHECK BALANCE
    # ==============================
    elif option == "6":

        print("\n========== 💳 CHECK BALANCE ==========")

        found = False

        if not account:
            print("❌ No accounts yet.")

        else:

            Search_Account = int(
                input("Enter Account number: ")
            )

            for acco in account:

                if Search_Account == acco["Account_no"]:

                    print("\n✅ Account found!")

                    print(
                        f"Account Holder: {acco['Name']}"
                    )

                    print(
                        f"Account No: {acco['Account_no']}"
                    )

                    print(
                        f"Balance: Rs.{acco['Balance']}"
                    )

                    found = True
                    break

            if not found:
                print("❌ Account not found.")


    # ==============================
    # 7. DELETE ACCOUNT
    # ==============================
    elif option == "7":

        print("\n========== 🗑️ DELETE ACCOUNT ==========")

        found = False

        if not account:
            print("❌ No accounts yet.")

        else:

            Search_Account = int(
                input("Enter Account number: ")
            )

            for acco in account:

                if Search_Account == acco["Account_no"]:

                    print("\n✅ Account found!")

                    print(
                        f"Account Holder: {acco['Name']}"
                    )

                    confirm = input(
                        "Are you sure? (yes/no): "
                    )

                    if confirm.lower() == "yes":

                        account.remove(acco)

                        print(
                            "✅ Account deleted successfully!"
                        )

                    else:

                        print(
                            "❌ Account deletion cancelled."
                        )

                    found = True
                    break

            if not found:
                print("❌ Account not found.")


    # ==============================
    # 8. EXIT
    # ==============================
    elif option == "8":

        print("\n╔══════════════════════════════════════╗")
        print("║ 👋 Thank you for using Bank System! ║")
        print("║      Program exited successfully.   ║")
        print("╚══════════════════════════════════════╝")

        break


    # ==============================
    # INVALID OPTION
    # ==============================
    else:

        print("\n❌ Invalid option!")
        print("Please choose between 1 and 8.")