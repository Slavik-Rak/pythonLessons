# Напишите программу, которая считывает со стандартного ввода целые числа,
# по одному числу в строке, и после первого введенного
# нуля выводит сумму полученных на вход чисел.
# a = 0
# while True:
#     n = int(input("Enter number: "))
#     if n != 0:
#         a += n
#     else:
#         break
# print(a)
# ---------------------------------------------------------------
# Напишите программу, которая считывает целые числа с консоли по одному числу в строке.
#
# Для каждого введённого числа проверить:
# если число меньше 10, то пропускаем это число;
# если число больше 100, то прекращаем считывать числа;
# в остальных случаях вывести это число обратно на консоль в отдельной строке.

# a = 0
# while True:
#     n = int(input("Enter number: "))
#     if n < 10:
#         continue
#     elif n > 100:
#         break
#     else:
#         print(n)
# ---------------------------------------------------------------
# Напишите программу, которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a;b],
# которые кратны числу 3.
#
# В приведенном ниже примере среднее арифметическое считается для чисел на отрезке [−5;12].
# Всего чисел, делящихся на 3, на этом отрезке 6: −3,0,3,6,9,12.
# Их среднее арифметическое равно 4.5.
# На вход программе подаются интервалы,
# внутри которых всегда есть хотя бы одно число, которое делится на 3.

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# count = 0
# number = 0
# for a in range(a, b + 1):
#     if a % 3 == 0:
#         number += a
#         count += 1
# print(number / count)

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# lst = []
# for a in range(a, b + 1):
#     if a % 3 == 0:
#         lst.append(a)
# print(sum(lst) / len(lst))
# ---------------------------------------------------------------

# GC-состав является важной характеристикой геномных
# последовательностей и определяется как процентное соотношение суммы
# всех гуанинов и цитозинов к общему числу нуклеиновых
# оснований в геномной последовательности.
#
# Напишите программу, которая вычисляет процентное содержание
# символов G (гуанин) и C (цитозин) в введенной строке
# (программа не должна зависеть от регистра вводимых символов).
#
# Например, в строке "acggtgttat" процентное содержание символов G и C равно 4/10⋅100=40.0,
# где 4 - это количество символов G и C,  а 10 - это длина строки.

# word = input("Enter: ")
# countG = 0
# countC = 0
# lst = []
# for i in word:
#     lst.append(i)
#     if i == "g" or i == "G":
#         countG += 1
#     elif i == "c" or i == "C":
#         countC += 1
#
# print(((countG + countC) / len(lst)) * 100)

# info = input()
#
# g = ""
# c = ""
# for item in info:
#     if item == "g" or item == "G":
#         g += item
#     if item == "c" or item == "C":
#         c += item
#
# count_g = len(g)
# count_c = len(c)
#
# final = (((count_g + count_c) / len(info)) * 100)
#
# print(final)


# Узнав, что ДНК не является случайной строкой,
# только что поступившие в Институт биоинформатики студенты группы
# информатиков предложили использовать алгоритм сжатия,
# который сжимает повторяющиеся символы в строке.
#
# Кодирование осуществляется следующим образом:
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2',
# то есть группы одинаковых символов исходной строки заменяются на этот
# символ и количество его повторений в этой позиции строки.
#
# Напишите программу, которая считывает строку,
# кодирует её предложенным алгоритмом и выводит закодированную
# последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.
#
#
# dnk = input("Enter: ")
# count = 1
# x = 0
# for i in dnk[x:]:
#     # print(dnk[x:], "  dnk[x:]")
#     if len(dnk) == x - 1:
#         print(i, end="")
#         print(count, end="")
#     j = dnk[x+1:]
#     for j in dnk[x+1:]:
#         if i == j:
#             count += 1
#         else:
#             print(i, end="")
#             print(count, end="")
#             break
#     x += count
#     count = 1


# dnk = input("Enter: ")
# counter = 1
# x = 1
# j = dnk[x:x+1]
# # print(j)
# for i in dnk:
#     if i in j:
#         counter += 1
#     else:
#         print(i, end="")
#         print(counter, end="")
#         counter = 1
#     x += 1
#     # print(j)
#     j = dnk[x:x+1]
#     print(j)

# 1) Напишите программу, на вход которой подается одна строка с целыми числами.
# Программа должна вывести сумму этих чисел.
#
# Используйте метод split строки.

# str = input("Enter number: ")
# n = str.split()
# print(n)
# sum = 0
# for i in n:
#     sum += int(i)
#     print(i)
# print(sum)

# for i in n[0]:
#     print(i)
#     sum += int(i)
# print(sum)


# 2) Напишите программу, которая считывает с консоли числа
# (по одному в строке) до тех пор, пока сумма введённых чисел не будет
# равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.
#
# Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0,
# после этого считывание продолжать не нужно.

# sum = 0
# sumPow = 0
# while True:
#     n = int(input("Enter number: "))
#     sum += n
#     sumPow += n**2
#     if sum == 0:
#         break
# print(sumPow)

# 3) Напишите программу, которая считывает список чисел lst из первой
# строки и число x из второй строки, которая выводит все позиции,
# на которых встречается число x в переданном списке lst.
#
# Позиции нумеруются с нуля, если число x не встречается в списке,
# вывести строку "Отсутствует" (без кавычек, с большой буквы).

# Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.

# lst = []
# while True:
#     n = input("Enter number: ")
#     lst.append(n)
#     if n == "!":
#         lst.pop(-1)
#         break
# number = int(input("Enter search number"))
# ind = 0
# count = 0
# for i in lst:
#     if int(i) == number:
#         print(ind, end=" ")
#         count += 1
#     ind += 1
# if count == 0:
#     print("Отсутствует")
#

# 1. Создать произвольный список
# 2. Добавить новый элемент типа str в конец списка-
# 3. Добавить новый элемент типа int на место с индексом
# 4. Добавить новый элемент типа list в конец списка
# 5. Добавить новый элемент типа tuple на место с индексом
# 6. Получить элемент по индексу
# 7. Удалить элемент
# 8. Найти число повторений элемента списка
# (1,2,3)

# lst = [1, 3, "qwe", True]
# lst.append("String")
# print(lst)
# lst[3] = 3
# print(lst)
# lst.append([9, 7, 0])
# print(lst)
# lst[0] = (1, 2, 3)
# print(lst)
# print(lst[3])
# lst.pop(0)
# print(lst)
#
# print(lst.count(3))
#

i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(i)
print(i[:2])
print(i[1:])
print(i[1:9])
print(i[1:9:2])
print(i[::])