# numbers = [1, 2, 3, 4, 5]
#
# print(numbers)
# print(type(numbers))
#
# names = ["Slavik", "Kristina", "Sasha"]
# print(names)

# test1 = []
# print(test1)
#
# test2 = list()
# print(test2)

# object = ["str", 1, 2.3, True, [1, 2, 3]]
# print(object)

# numbers1 = [1, 2, 3, 4, 5]
# numbers2 = list(numbers1)
# numbers3 = numbers2
# print(numbers3)

# a = input("test: ")
# b = list(a)
# print(b)

# numbers = ["www", 2] * 6
# print(numbers)

# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# print(numbers[-2])
#
# numbers[0] = 10
# print(numbers)

# names = ["Slavik", "Sasha", "Sofia"]

# n1, n2, n3 = names
# print(n1)

# for i in names:
#     print(i)

# i = 0
# while i < len(names):
#     print(names[i])
#     i += 1

# print(len(names))

# name = "Veronika"
#
# print(len(name))

# методи

# people = ["Sasha", "Sofia", "Veronika", "Sasha"]
# print(people)
# people.append("Slavik") # Додає елемент в кінець ліста
# people.append("Slavik")
# print(people)
# people.insert(0, "Kristina") # додає елемент по заданому індексу
# print(people)
# people.extend([1, 2, 3]) # додає ліст в кінець ліста
# print(people)
#
# print(people.index("Sasha")) # повертає індекс елемента
#
# people.pop(7) # видаляє по заданому індексу
# print(people)

# people.remove(2) # видаляє елемент
# print(people)
#
# print(people.count("Sasha")) # повертає кількість одинакових елементів

# numbers = [1, 8, 3, 2, 5]
# numbers.reverse() # обертає ліст
# print(numbers)
# numbers.sort() # сортує ліст
# print(numbers)

# numbers.clear() # очищає ліст
# print(numbers)

# print(len(numbers))
#
# print(sorted(numbers)) # сортує ліст (можна в принті)
# print(min(numbers))
# print(max(numbers))

# people = ["Tom", "Bob", "Alice", "Sam"]
# name = input("Enter some name: ")
#
# if people.count(name):
#     print(True)
# else:
#     print(False)

# if name in people:
#     print(True)
# else:
#     print(False)

# Напишите программу, которая получает на вход три целых числа,
# по одному числу в строке, и выводит на консоль в три строки сначала максимальное,
# потом минимальное, после чего оставшееся число.

# На ввод могут подаваться и повторяющиеся числа.
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
#
# ls = [a, b, c]

# print(max(ls))
# print(min(ls))
#
# ls.remove(max(ls))
# ls.remove(min(ls))
# print(ls[0])

#
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
#
# ls = [a, b, c]
#
# ls.sort()
# print(ls)
# print(ls[-1])
# print(ls[0])
# print(ls[1])

ls = [1, 2, 3, 4, 5, 6]
print(ls[1:3])









