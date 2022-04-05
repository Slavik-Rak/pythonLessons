
a = int(input("Enter number: "))

if a == 0 or a > 1000:
    print("Error enter")
else:
    if a % 10 == 1 and a % 100 != 11:
        print(a, " програміст")
    elif 2 <= a % 10 <= 4 and 12 >= a % 100 >= 14:
        print(a, " програмістa")
    else:
        print(a, " програмістів")

