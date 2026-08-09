print("=" * 50)
print(" 🏧    ATM MANAGEMENT SYSTEM    🏧 ")
print("=" * 50)

print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Transaction History")
print("5. Transfer")

print("6. Exit")
print("7. Change PIN")
print("8. Fast Cash")

balance = 100000
transaction_history = []
confirm = 0
pin = 1234
pin_attempts = 3
pin_verified = False

Account_number = int(input("Enter Account Number"))
 
if Account_number == 123456789:
    print("Account Number Correct?")
else:
    print("❌ Invalid Account Number")
    exit()








# ---------------- PIN Verification ---------------- #

while pin_attempts > 0:
    user_pin = int(input("Enter your 4-digit PIN: "))

    if user_pin == pin:
        print("✅ PIN Verified Successfully!")
        pin_verified = True
        break
    else:
        pin_attempts -= 1
        print(f"❌ Wrong PIN! Attempts Left: {pin_attempts}")

if not pin_verified:
    print("🚫 Account Locked!")
    exit()

# ---------------- ATM Menu ---------------- #

while True:

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print(f"Your Balance: ₹{balance}")

    elif choice == "2":
        deposit = int(input("Enter amount to deposit: ₹"))
        balance += deposit
        transaction_history.append(f"Deposited ₹{deposit}")
        print("✅ Money Deposited Successfully!")
        print(f"New Balance: ₹{balance}")

    elif choice == "3":
        withdraw = int(input("Enter amount to withdraw: ₹"))

        if withdraw <= balance:
            balance -= withdraw
            transaction_history.append(f"Withdrawn ₹{withdraw}")
            print("✅ Money Withdrawn Successfully!")
            print(f"Remaining Balance: ₹{balance}")
        else:
            print("❌ Insufficient Balance!")

    elif choice == "4":
        if len(transaction_history) == 0:
            print("📜 No Transactions Yet!")
        else:
            print("\n📜 Transaction History")
            print("=" * 30)

            for i in range(len(transaction_history)):
                print(f"{i+1}. {transaction_history[i]}")

            print("=" * 30)
     
     
    elif choice == "5":
        transfer = int(input("Enter amount to transfer: ₹"))
        if transfer <= balance:
            balance -= transfer
            transaction_history.append(f"Transferred ₹{transfer}")
            print("✅ Money Transferred Successfully!")
            print(f"New Balance: ₹{balance}")
        else:
            print("❌ Insufficient Balance!")

    elif choice == "6":
        print("\n👋 Thank you for using our ATM.")
        print("Have a Nice Day!")
        break
    elif choice == "7":
        user_pin = int(input("Enter your 4-digit PIN: "))
        if user_pin == pin:
            new_pin = int(input("Enter the new 4-digit PIN: "))
            confirm = int(input("Confirm your new 4-digit PIN: "))
            if confirm == new_pin:
                pin = new_pin
                print("PIN Changed Successfully")
            else:
                print("❌ New PIN and Confirm PIN do not match!")
        else:
            print("❌ Incorrect PIN. PIN change failed.")

    elif choice == "8":

    elif choice == "8":
     while True:
        print("1. ₹500")
        print("2. ₹1000")
        print("3. ₹2000")
        print("4. 5000")
        print("5. back")
        fast_cash = 0
    
        option = int(input(" Please the choose 1-5. :-"))
        if option ==  1:
            fast_cash = 500
        elif option  == 2:
            fast_cash = 1000
        elif option == 3:
            fast_cash = 2000
        elif option  == 4:
            fast_cash =5000
        elif option  == 5:
            print("Returning to Main Menu...")
            break
        else:
            print(" Invalid Fast Cash Option!")
            continue
            
            
            
        if fast_cash <= balance:
            balance -= fast_cash
            transaction_history.append(f"Fast Cash Withdrawal ₹{fast_cash}")
            print("fast Cash Withdrawal Successful!")
            print(f"💵 Please collect your cash.💰")
            print(f"Remaining Balance: ₹{balance}")
            print("Thank you for using our ATM.")
            break
            
             
        else:
             print("Insufficient Balance!")
             
             
    else:
        print("❌ Invalid Choice! Please enter a valid option (1-6).")