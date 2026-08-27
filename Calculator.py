print("======================")
print(" Python calcullator")
print("==========================")

print("1. Addition")
print("2.  Subtraction ")
print("3.  Multiplication  ")
print ("4. Division")
print(" 5. Modulus")
print("6.  power")
print("7. History")

history = []
while True:
    option = input("Enter your option :-")
    if option == "1":
        num1 = float(input("Enter your first number :-"))
        num2 = float(input( "Enter your sec  number :-"))
        result = num1 + num2 
        print(f"Rueslt : {result}")
        history.append(f" {num1} + {num2} = {result}")
    elif option == "2":
        num1 = float(input("Enter your first number :-"))
        num2 = float(input( "Enter your sec  number :-"))
        result = num1 - num2
        print(f"result : {result}")
        history.append(f" {num1} - {num2} = {result}")
    elif option == "3":
        num1 = float(input("Enter your first number :-"))
        num2 = float(input( "Enter your sec  number :-"))
        result = num1 * num2
        print(f"Rueslt : {result}")
        history.append(f" {num1} \* {num2} = {result}")
    elif option == "4":
        num1 = float(input("Enter your first number :-"))
        num2 = float(input( "Enter your sec  number :-"))
        if num2 == 0:

            print("❌ Cannot use zero!")

            continue

        result = num1 / num2
        print(f"Rueslt : {result}")
        history.append(f"{num1} / {num2} = {result}")

    elif option == "5":
            num1 = float(input("Enter your first number :-"))
            num2 = float(input( "Enter your sec  number :-"))
            if num2 == 0:
    
                print("❌ Cannot use zero!")
    
                continue
    
            result = num1 % num2
            print(f"Rueslt : {result}")
            history.append(f"{num1} % {num2} = {result}")
    elif option == "6":
          num1 = float(input("Enter your first number :-"))
          num2 = float(input( "Enter your sec  number :-"))
          result = num1 ** num2
          print(f"Rueslt : {result}")
          history.append(f"{num1} ** {num2} = {result}")
    elif option == "7":
        if not history:
            print("there no histor yet")
            
         for i in history:
              print(i)
         

           
    

        
