# using simple if else condition 

#  age = int(input("enter your age: "))

# if age>=18:
#     print("eligible for vaccination ")
# else :
#     print("not eligible")    


# nested if

# age = int(input("enter your age: "))
# registration = input("enter your answer: ")

# if age>=18:
#     if registration == "yes":
#         print("eligible for vaccination ")
# else :
#     print("not eligible")    

# COVID VACCINATION FORM 

# print(".....COVID Vaccination Form.....")

# name = input("Enter Name: ")
# age = int(input("Enter Age: "))
# gender = input("Enter Gender: ")
# mobile = input("Enter Mobile Number: ")
# vaccine = input("Enter Vaccine Name (Covaxin/Covishield): ")
# dose = input("Enter Dose (1st/2nd/Booster): ")

# print("\n----- Vaccination Details -----")
# print("Name:", name)
# print("Age:", age)
# print("Gender:", gender)
# print("Mobile Number:", mobile)
# print("Vaccine:", vaccine)
# print("Dose:", dose)

# if age >= 18:
#     print("Status: Eligible for Vaccination")
# else:
#     print("Status: Not Eligible for Vaccination")

# using exception handling with else 

print(".....COVID Vaccination Form.....")

try:

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    mobile = input("Enter Mobile Number: ")
    vaccine = input("Enter Vaccine Name (Covaxin/Covishield): ")
    dose = input("Enter Dose (1st/2nd/Booster): ")

    if age >= 18:
       print("Status: Eligible for Vaccination")
except (ValueError, NameError, TypeError) : 
    print ("invalid age input provided as per errors ")  
else:
    print("valid inputs ")    
