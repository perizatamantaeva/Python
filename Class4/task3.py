sum = 0

for number in range(1, 101):
    sum += number

print("The sum of numbers from 1 to 100 is:", sum)

for counter in range(100, 0, -1):
    print(counter)
numbers = list(range(0, 11))

for number in numbers:
    if number % 2 == 0:
        print(number)

number = int(input("Enter a number: "))

for i in range(11):
    result = number * i
    print(f"{number} * {i} = {result}")
