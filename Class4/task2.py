numbers = []
total = 0

while total < 100:
    value = int(input("Enter an integer value: "))
    numbers.append(value)
    total = sum(numbers)

print("Condition met! The sum of the numbers is 100 or above.")
print("All numbers entered:", numbers)


# sum = 0
# list1 = []

# while sum < 100:
#     number = int(input("Enter number: "))
#     sum = sum + number
#     list1.append(number)

# print(f"Here is a list: {list1}")