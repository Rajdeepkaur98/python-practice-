# ----------Calculator----------

# print(".....Calculator.....")
# while True: 
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))

#     op = input("Enter operator (+, -, *, /,>): ")
#     if op == "+":
#         print("Result =", num1 + num2)
#     elif op == "-":
#         print("Result =", num1 - num2)
#     elif op == "*":
#         print("Result =", num1 * num2)
#     elif op == "/":
#         print("Result =", num1 / num2)
#     elif op == ">":
#         print("result =", num1> num2)    

# else:
#     print("Invalid Operator")


# ----------ATM-----------
#  
balance = 5000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Balance =", balance)

    elif choice == "2":
        amount = int(input("Enter amount: "))
        balance = balance + amount
        print("Money Deposited")

    elif choice == "3":
        amount = int(input("Enter amount: "))
        if amount <= balance:
            balance = balance - amount
            print("Money Withdrawn")
        else:
            print("Insufficient Balance")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")    