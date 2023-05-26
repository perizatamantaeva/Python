# def add_numbers(num1, num2):
#     return num1 + num2

# def subtract_numbers(num1, num2):
#     return num1 - num2

# def multiply_numbers(num1, num2):
#     return num1 * num2

# def divide_numbers(num1, num2):
#     return num1 / num2


# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# operation = input("Enter the operation (+, -, *, /): ")

# if operation == "+":
#     result = add_numbers(num1, num2)
# elif operation == "-":
#     result = subtract_numbers(num1, num2)
# elif operation == "*":
#     result = multiply_numbers(num1, num2)
# elif operation == "/":
#     result = divide_numbers(num1, num2)
# else:
#     print("Invalid operation!")
#     exit()

# print("Result:", result)


def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def multiply_numbers(num1, num2):
    return num1 * num2

def divide_numbers(num1, num2):
    return num1 / num2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Enter the operation (+, -, *, /): ")

operations = {
    "+": add_numbers,
    "-": subtract_numbers,
    "*": multiply_numbers,
    "/": divide_numbers
}

if operation in operations:
    result = operations[operation](num1, num2)
    print("Result:", result)
else:
    print("Invalid operation!")
