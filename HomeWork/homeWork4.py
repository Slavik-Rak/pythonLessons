# 1) Задача. Пользователь вносит указанную сумму на указанное
# количество лет под 10% годовых. Вернуть сумму которая будет на счете в конце срока.
#
# ! Проценты начисляются на остаток на счете каждый год.
#

# def deposit(moneys, years, months):
#     if months == 0 and years == 0:
#         print("You not enter time!!!! ")
#     elif months == 0 and years > 0:
#         while years != 0:
#             moneys += (moneys / 100) * proc
#             years -= 1
#         return moneys
#     elif months > 0 and years == 0:
#         while months != 0:
#             moneys += (moneys / 100) * procMonth
#             months -= 1
#         return moneys
#     elif months > 0 and years > 0:
#         timeMonths = (years * 12) + months
#         while timeMonths != 0:
#             moneys += (moneys / 100) * procMonth
#             timeMonths -= 1
#         return moneys
#
#
# moneys = int(input("Enter moneys: "))
# proc = 10
# procMonth = proc / 12
#
# if moneys <= 0:
#     print("No moneys!!!!")
# else:
#     years = int(input("Enter years: "))
#     months = int(input("Enter months: "))
#
#     print(deposit(moneys, years, months))

# --------------------------------------------------------
# 2) Требуется создать функцию list_sort(lst), которая сортирует список
# чисел по убыванию их абсолютного значения.
# Для решения потребуется метод sort(), в который передается функция,
#  определяющая абсолютное значение.

