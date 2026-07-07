# zerodivisionerror
# try:
#     a=int(input("enter a number: "))
#     print(100/a)
# except ZeroDivisionError:
#     print("non divisible number ")    

# valueError 
# try:
#     age= int(input("enter age: "))
#     print("valid")
# except ValueError:
#     print("invalid ")      

# type error
# try:
#     a = int(input("enter a number: ")) 
#     b = input("enter the value: ")
#     print("valid",a+b)
# except TypeError:
#     print("invalid ")    

# try:
#     a = int(input("enter a number: ")) 
#     b = int(input("enter the value: "))
#     print("valid",a+b)
# except TypeError:
#     print("invalid ")      

# file not found error
# try: 
#     file = open("demo.txt","r")
#     print("valid ")
# except FileNotFoundError:
#     print("invalid filename")    

# name error 
# try: 
#     print(x)
# except NameError:
#     print("invalid" )   



# using else
# try:
   
#     a=int(input("enter a number: "))
#     print(100/a)
# except ZeroDivisionError:
#     print("non divisible number ") 
# else :
#     print("the number is divisible")    


# -----ATM using Exception Handling-----

try:
    while True:
       print("-----bank menu-----")
       print("1. deposit")
       print("2. withdraw")
       print("3. balance")
       print("4. exit ")
    name = input("enter your name: ")
    if name == "rajdeep" :

     password = int(input("enter you password: "))
    if password == 12345:

        amount = int(input("enter the withdrawal amount: "))
        if amount == 5000:
            print("withdraw successful")
except ValueError:
   print("invalid values entered in the coloumn")
else:
   print("valid information ")   


# caclulator 

# print(".....Calculator.....")

# try:
  
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
#     else:   
#         print("invalid operator ")
       
# except ( ValueError, ZeroDivisionError):
#     print("invalid detail, errors occured  ")
# else:
#     print("valid details")