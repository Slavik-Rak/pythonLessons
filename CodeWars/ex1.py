# наша задача состоит в том, чтобы сделать функцию,
# которая может принимать любое неотрицательное
# целое число в качестве аргумента и возвращать его
# с его цифрами в порядке убывания. По сути,
# переставьте цифры, чтобы получить максимально возможное число.


def descending_order(num):
    if int(num) > 0:
        lst = []
        for i in num:
            lst += i
        print(lst)
        str = ""
        lst.sort(reverse=True)
        return int(str.join(lst))
    else:
        print("ERRORS")


m = input("n: ")

descending_order(m)
