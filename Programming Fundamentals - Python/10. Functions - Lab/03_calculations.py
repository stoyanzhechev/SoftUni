def calculation(operator):
    if operator == 'add':
        return first_number + second_number
    elif operator == 'subtract':
        return first_number - second_number
    elif operator == 'multiply':
        return first_number * second_number
    elif operator == 'divide':
        return int(first_number / second_number)


operator = input()
first_number = int(input())
second_number = int(input())
print(calculation(operator))