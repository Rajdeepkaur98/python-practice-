# module
# print("..calendar..")
# import calendar

# print(calendar.calendar(2025))
# print(calendar.month(2025,1))
# print(calendar.isleap(2026))
# print(calendar.weekday(2026, 6, 25)) // 0= monday ,......, 6= sunday
# print(calendar.month_name[1])

# year = int(input("Enter year: "))
# month = int(input("Enter month: "))

# print(calendar.month(year, month))

# year = int(input("Enter year: "))

# print(calendar.calendar(year))

# year = int(input("Enter year: "))

# if calendar.isleap(year):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

# file handling 

# file = open("hello.txt", "r")
# print(file.read())
# file.close()

file = open("hello.txt", "w")
file.write("Hello Python")
file.close()

file = open("hello.txt", "r")
print(file.read())
file.close()

file = open("hello.txt", "w")
file.write("A programming language")
file.close()

file = open("hello.txt", "a")
file.write("\npython")
file.close()

file = open("file.txt", "x")
file.write("hello python")

file.close()