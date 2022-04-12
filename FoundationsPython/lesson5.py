# def say_hello():
#     print("Hello!")
#
#
# say_hello()
# say_hello()
# say_hello()
# say_hello()

# def print_massages():
#     def say_hello():
#         print("Hello!")
#
#     def say_goodbay():
#         print("Goodbay!")
#     say_hello()
#     say_goodbay()
#
#
# print_massages()
# def main():
#     say_hello()
#     say_goodbye()
#
#
# def say_hello():
#     print("Hello!")
#
#
# def say_goodbye():
#     print("Goodbye!")
#
#
# main()

# def say_hello(name):
#     print("Hello", name)
#
#
# say_hello("Slavik")
#
# def name_age(name, age):
#     print("Name:", name, "Age:", age)
#
#
# n = input("Enter name: ")
# a = int(input("Enter age: "))
#
#
# name_age(n, a)

# def say_massages(name="None", age=18):
#     print(name, age)
#
#
# say_massages(age=25)

# def sum(*numbers):
#     r = 0
#     for i in numbers:
#         r += i
#     return r
#
#
# print(sum(1, 2, 3, 4, 5))

# age    if 1<age<100

def check_age(age):
    if 1 < age < 100:
        return True
    else:
        return False


check = check_age

print(check(18))
# print(type(check(18)))


# def try_operation(a, b, operation):
#     result = operation(a, b)
#     print(result)
#
#
# def sum(a, b):
#     return a + b
#
#
# def multiplay(a, b):
#     return a * b
#
#
# try_operation(5, 4, sum)
#
# try_operation(5, 4, multiplay)

# -------------------------
#
# def sum(a, b):
#     return a + b
#
#
# def multiplay(a, b):
#     return a * b
#
#
# def select_operation(choice):
#     if choice == 1:
#         return sum
#     else:
#         return multiplay
#
#
# opration = select_operation(1)
# print(opration(10, 6))
#
# opration = select_operation(0)
# print(opration(10, 6))