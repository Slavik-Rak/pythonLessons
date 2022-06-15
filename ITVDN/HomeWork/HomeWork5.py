# Задание 1
# Есть список а = [2, 4, 65, 32, 2, 6, 0, -1, 3]. Вывести все значения меньше 5 в консоль
# а = [2, 4, 65, 32, 2, 6, 0, -1, 3]
#
# for elem in а:
#     if elem < 5:
#         print(elem)

# Задание 2
# “aabbаа” - палиндром. Как это проверить
# myList = list('11aabbаа')
#
# listRevers = []
# for elem in myList:
#     print(elem)
#     listRevers.append(elem)
#
# listRevers.reverse()
# print("Reuslt is: ",listRevers)
#
# if listRevers == myList:
#     print("PALINDROME")
# else:
#     print("NO PALINDROME")


# print(myList)
# print(listRevers)

# Задание 2
# Есть список a = [1, 3, 9, 13, 7, 8, 13, 32, 44, 59, 19].
# Выведите все элементы, которые меньше 6.
# a = [1, 3, 9, 13, 7, 8, 13, 32, 44, 59, 19]
# for elem in a:
#     if elem < 6:
#         print(elem, end=" ")

# Задание 3
# На основании списка a = [‘red’, ‘yellow’, ‘blue’, ‘bread’]
# Создать список, в котором будет только слово, лишнее в списке a.


# a = ["red", "yellow", "blue", "bread"]
# b = a.pop(-1)
# print(b)
# print(a)

d = {"a": 10, "b": 5, "c": 7}
s = ""

for x in d:
    s += x

print(s)






