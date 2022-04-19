# try:
#     a = int(input("Enter num1: "))
#     b = int(input("Enter num2: "))
#     print(a / b)
# except ZeroDivisionError:
#     print("Div 0!!!!!!!")
# except ValueError:
#     print("String!!!")


# try:
#     a = int(input("Enter num1: "))
#     b = int(input("Enter num2: "))
#     print(a / b)
# except (ZeroDivisionError, ValueError):
#     print("Errors!!!")


# try:
#     a = int(input("Enter num1: "))
#     b = int(input("Enter num2: "))
#     print(a / b)
# except Exception:
#     print("Errors Exception")


# try:
#     a = int(input("Enter num1: "))
#     b = int(input("Enter num2: "))
#     print(a / b)
# except ValueError as e:
#     print("info my error ", e)
#

# Напишите программу, которая запрашивает ввод двух значений.
# Если хотя бы одно из них не является числом, то должна выполняться конкатенация,
# то есть соединение, строк. В остальных случаях введенные числа суммируются.

a = 1
b = 2

if int(a) and int(b):

