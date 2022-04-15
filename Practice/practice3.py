# Пользователь вводит номер месяца, функция возвращает время года.
#
# def season(m):

# numberMon = int(input("Enter number month: "))
#
#
# def season(x):
#     if 0 < x <= 12:
#         if 11 < x <= 12:
#             print("Winter!")
#         elif 2 < x <= 5:
#             print("Spring!")
#         elif 5 < x <= 8:
#             print("Summer!")
#         else:
#             print("Autum!")
#
#
# season(numberMon)

# Задача. Пользователь вводит предложение(какой-либо текст).
# Программа вычисляет самое длинное слово в предложении.?

# txt = input("Enter Text: ")
#
#
# def searchLongWorld(x):
#     x = x.replace(",","")
#     count = x[0]
#     lst = x.split()
#
#     for i in lst:
#         if len(i) > len(count):
#             count = i
#     print(count)
#
#
# searchLongWorld(txt)
# ++++++++++++++++++++++++++
# s = input("Enter Text: ")
#
# n = max(s.replace(",","").split(), key=len)
# print(n)
#-----------random--------------------------
# import random
#
# lst1 = []
# lst2 = []
# a = 10
# for i in range(a):
#     lst1.append(i)
#     lst2.append(random.randrange(0,10))
# print(lst1)
# print(lst2)
#-----------random--------------------------

# Задача. Создать список, заполнить список случайными целыми
# числами в указанном диапазоне и отсортировать список по возрастанию и убыванию.
#
# Пользователь вводит нижний и верхний диапазон чисел и количество элементов списка.
# import random
#
# min = int(input("Enter Min number: "))
# max = int(input("Enter Max number: "))
# count = int(input("Enter Count list: "))
#
#
# def sort_list(a, b, c):
#     lst = []
#     while c > 0:
#         lst.append(random.randrange(a, b))
#         c -= 1
#     print(sorted(lst))
#     lst.sort(reverse=True)
#     print(lst)
#
#
# sort_list(min, max, count)


