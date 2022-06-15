# Напишите программу, используя знания о переменных типа целых чисел, чтобы посчитать за
# какое время транспортное средство доедет из пункта А в пункт В, если известны следующие
# данные: расстояние от А до В = 250 км, скорость автомобиля будет постоянной и равна 80 км/ч.
# Используйте формулу: Время = расстояние / скорость. Создайте переменные length, куда
# запишите расстояние, velocity, куда запишите скорость и переменную time, куда запишите
# результат. После чего используйте метод print(), чтобы вывести в консоль результат.
#
# length = 250
# velocity = 80
# time = (length / velocity)
# print(time)
#
# Задание 2
# Создайте переменную age = 25, переменную name = “John”. Выведите в консоль “My name is
# <name> and I am <age>”, но сделайте решение таким, чтобы использовалась конкатенация
# строк (через +) и приведение типа числа к строке (str(...)). То есть, чтобы если заменить
# переменные age и name, то в методе print() ничего не нужно было менять. Например a = 10,
# # print(“Value =” + str(a)) и будет “Value = 10
#
# age = 25
# name = "John"
# print("my name is " + str(name) + " and I am " + str(age))


string = '''Lorem {} ipsum dolor sit amet,
consectetur
adipiscing
elit, {}
do
eiusmod
tempor
incididunt
ut
labore
et
dolore
magna
aliqua.
'''
#
# x = 1
#
# b = "hello"
#
# if len(b) == len(b * x):
#     print(1)
#
# if len(b) * 2 < len(b):
#     print(2)
#
# elif x > 0:
#     print(3)
#
# else:
#     print(4)
#
# if x * x > x ** x:
#     print(5)
for number in range(11):
    if number % 2 == 0:
        print("Current number is", number)
    else:
        continue







