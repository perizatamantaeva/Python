# tip = 0
# while tip != 14.99 or tip !=19.99:
#     tip = int(input("Please enter tip amount: "))

# if tip == 14.99:
#     print("Standard")

# elif tip == 19.99:
#     print("Good")

# Loop should continue until you enter 14.99 that should print Standard, and 19.99 that should print Good
#error


tip = 0
while tip != 14.99 and tip !=19.99:
    tip = float(input("Please enter tip amount: "))


if tip == 14.99:
    print("Standard")

elif tip == 19.99:
    print("Good")