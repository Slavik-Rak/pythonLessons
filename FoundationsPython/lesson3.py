# city = input("Enter name city : ")
#
# if city == "Kiev":
#     print("Kiev")
# elif city == "Lviv":
#     print("Lviv")
# else:
#     print("Not city")


city = input("Enter city: ")


if city == "Lviv":
    print("Lviv")
    dayTime = input("Enter Time: ")
    if dayTime == "morning":
        print("good morning, Lviv")
    elif dayTime == "evening":
        print("good evening, Lviv")
    else:
        print("None day time")
elif city == "Kiev":
    print("Kiev")
    dayTime = input("Enter Time: ")
    if dayTime == "morning":
        print("good morning, Kiev")
    elif dayTime == "evening":
        print("good evening, Kiev")
    else:
        print("None time day")
else:
    print("None City")