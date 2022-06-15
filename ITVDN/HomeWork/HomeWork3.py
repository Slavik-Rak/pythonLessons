# Задание 1
# Вывести в консоль первые 100 чисел Фибоначчи (см. в рекомендованных ресурсах)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,

# num1 = 1
# num2 = 1
# print(num1)
# print(num2)
# counter = 10
# while counter > 0:
#     num3 = num1 + num2
#     num1 = num2
#     num2 = num3
#     print(num3)
#     counter -= 1

# Задание 2
# В предложении “Hello world” заменить все буквы “o” на “a” , а буквы “l” на “e”.
# fraz = "Hello world"
# newFraz = ""
# n = len(fraz)
# print(n)
# for i in range(n):
#
#     if fraz[i] == "o":
#         newFraz += "a"
#     elif fraz[i] == "l":
#         newFraz += "e"
#     else:
#         newFraz +=fraz[i]
#
# print(newFraz)

# Задание 3
# Создайте любую переменную строку и поместите туда любой текст. Сделайте так, чтобы все
# нечетные по порядку слева на право символы стали “_”, а все символы, местоположение
# которых четное и которые равны “a” - стали “b”. Например “Ham is tasty” => “_b_ _s_t_s_y”
# str = input("Enter sum text: ")
# l = len(str)
# strNew = ""
# for i in range(l):
#     if i % 2 == 0:
#         strNew += "_"
#     else:
#         if str[i] == "a":
#             strNew += "b"
#         else:
#              strNew += str[i]
# print(strNew)

# Задание 2
# Пройтись по диапазону чисел от 0 до 100 и вывести только те из них, которые делятся на 3

# for i in range(100):
#     if i % 3 == 0:
#         print(i)

#Задание 3
# Пройтись по диапазону чисел от 0 до 100, выводить все числа, при этом пропустить число 4 и,
# как только цикл достигнет числа 18 - выйти из цикла.

# for i in range(100):
#     if i == 4:
#         continue
#     if i == 18:
#         break
#     print(i)
#


for row in range(5):
    for column in range(5):
        print("*", end=" ")
        if column != 4:
            print(" ", end=" ")
    print()
