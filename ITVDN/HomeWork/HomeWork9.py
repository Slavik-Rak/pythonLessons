# Задание 1
# Напишите функцию, которая меняет значение глобальной переменной.
# x = 12
#
# def chenge():
#     global x
#     x = 4
#
# chenge()
# print(x)

# Задание 2
# Напишите рекурсивную функцию для того, чтобы посчитать значения факториала числа, которое
# передается аргументом (см. рекомендуемые ресурсы).

# def fuktor_number(x):
#     if x == 0:
#         return  1
#     else:
#         return x * fuktor_number(x - 1)
#
#
# print(fuktor_number(3))

# Дано натуральное число n. Выведите все числа от 1 до n.

# def rec_nat_num(n):
#     if n == 0:
#
#         return 1
#     else:
#         print(n)
#         return n - rec_nat_num(n-1)
#
# print(rec_nat_num(10))

# адание 2
# Напишите рекурсивную функцию для того, чтобы посчитать значения факториала числа, которое
# передается аргументом (см. рекомендуемые ресурсы).
#
# def fun_fatorial(n):
#     if n == 1:
#         return 1
#     else:
#         print(n)
#         return n * fun_fatorial(n - 1)
#
#
# print(fun_fatorial(10))

# Задание 3
# Найдите наибольшее значение в списке с помощью рекурсии.

list = [3, 6, 2, 3, 7, 0, -4, 6]
list1 = [2]
list2 = []


def fun_max_num_list(ls, max=None):
    if len(ls) == 0 and max == None:
        return "List Null"
    elif len(ls) == 1 and max == None:
        print("Max Number list :", ls[0])
        return ls[0]
    if max == None:
        max = ls.pop()
    comparison = ls.pop()
    if comparison > max:
        max = comparison
    if ls:
        return fun_max_num_list(ls, max)
    return max


print(fun_max_num_list(list))
print(fun_max_num_list(list1))
print(fun_max_num_list(list2))
