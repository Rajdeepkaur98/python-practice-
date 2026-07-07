# *nested loop with input field ( used when the 1st condition is wrong, no need to move forward as it shows the result at the same time when the condition invalids) *
# (input field - condition, then again input field - condition..... and at last else condition )

# name = input("enter your name: ")

# if name == "rajdeep" :
#     password = int(input("enter you password: "))
#     if password == 12345:
#         amount = int(input("enter the withdrawal amount: "))
#         if amount == 5000:
#             print("withdraw successful")
# else : 
#     print("not successful")            

# *nested loop with if-else ( used when to check the condition inside the if statement-> if, if-else [else for the particular condition], else [for whole condition,last else at end of the code]) *

# name = input("enter your name: ")
# password = int(input("enter you password: "))
# amount = int(input("enter the withdrawal amount: "))

# if name == "rajdeep" :
#     if password == 9899 : 
#         if amount <= 95000000:
#             print("withdraw successful")
#         else :
#             print("insufficient ")    
# else : 
#     print("not successful")  

# *nested loop ( simple nested if conditon, only one else at the end of the code for whole program condition check ) * 

# name = input("enter your name: ")
# password = int(input("enter you password: "))
# amount = int(input("enter the withdrawal amount: "))

# if name == "rajdeep" :
#     if password == 12345: 
#         if amount == 5000:
#             print("withdraw successful")
# else : 
#     print("not successful")  



balance = 10000
name = input("enter your name: ")
password= int(input("enter your password: "))

try:
    while True:
        print("-----bank menu-----")
        print("1. deposit")
        print("2. withdraw")
        print("3. balance")
        print("4. exit ") 
        choice = int(input("enter your choice :"))

        if choice==1:
            amount = int(input("enter the deposit amount: "))
            balance+=amount
            print("balance= ",balance)
        elif choice == 2 :
            amount=int(input("enter the withdraw amount: "))
            balance-=amount 
            print("balance= ",balance)
        elif choice==3:
            print("balance = ",balance)
        elif choice==4 :
            print("thankyou") 
            break
        else: 
            print("invalid choice entered") 
except ValueError :
    print("error in the values occured ")                   
