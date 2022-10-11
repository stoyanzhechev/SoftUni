def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    return int(first_number / second_number)


operator = input()
first_number = int(input())
second_number = int(input())

if operator == 'add':
    print(add(first_number, second_number))
elif operator == 'subtract':
    print(subtract(first_number, second_number))
elif operator == 'multiply':
    print(multiply(first_number, second_number))
elif operator == 'divide':
    print(divide(first_number, second_number))


