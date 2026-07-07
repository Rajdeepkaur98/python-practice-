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
