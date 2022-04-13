# 1 Напишите функцию sum_range(start, end),
# которая суммирует все целые числа от значения «start» до величины «end» включительно.
# Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.

# def sum_renge(start, end):
#     if start > end:
#         n = start
#         start = end
#         end = n
#
#     sum = 0
#     for i in range(start, end):
#         sum += i
#     return sum
#
#
# n = int(input("Enter start number: "))
# m = int(input("Enter end number: "))
# print(sum_renge(n, m))

# ----------------------------------------


# 2) Чтобы проверить понимание параметров и область их видимости, Николай создал 3 функции (представлены ниже).
# Попытайтесь предугадать, как поведет себя каждая из них при запуске (возникнут ли ошибки, что возвратится).

# def func1():
#     param = 4
#
#     def inner():
#         param += 1
#
#     return param
# ---------------------------------------
# вивід 4
# ---------------------------------------
#
# def func2():
#     param = 4
#
#     def inner(var):
#         var += 1
#
#     inner(param)
#     return param
# ---------------------------------------
# вивід 5
# ---------------------------------------
#
# def func3():
#     param = 4
#
#     def inner(var):
#         var += 1
#         return var
#
#     param = inner(param)
#     return param
# -----------------------------------------
# dbdsl 5
# -----------------------------------------

# 3) Создайте функцию three_args(), которая принимает 1, 2 или 3 строго ключевых параметра.
# В результате ее работы на печать в консоль выводятся значения переданных переменных, но только если они
# не равны None.
# Получим, например, следующее сообщение: «Переданы аргументы: var1 = 2, var3 = 10».

def three_args(var1="None", var2="None", var3="None"):
    if var1 == "None" and var2 == "None" and var3 == "None":
        print("Errors!!!")
    else:
        print("Переданы аргументы:", end="")
        if var1 != "None":
            print(" var1 =", var1, end="")
        if var2 != "None":
            print(" var2 =", var2, end="")
        if var3 != "None":
            print(" var3 =", var3, end="")



arg1 = input("Enter arg1: ")
arg2 = input("Enter arg2: ")
arg3 = input("Enter arg3: ")

three_args(arg1, arg2, arg3)
