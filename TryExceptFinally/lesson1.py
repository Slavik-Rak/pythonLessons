# str = "Hello"
#
# print(int(str))

try:
    numbr = int(input("Enter number: "))
    print(numbr)
except ValueError:
    print("ValueError")
finally:
    print("Try close")


print("Finish!")


