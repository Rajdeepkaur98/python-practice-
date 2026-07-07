# def my_decorator(func):
#     def wrapper():
#         print("Before function execution")
#         func()
#         print("After function execution")
#     return wrapper

# @my_decorator
# def greet():
#     print("Hello!")

# greet()


# # generators
def count():
    for i in range(1, 4):
        yield i

g = count()

for value in g:
    print(value)
