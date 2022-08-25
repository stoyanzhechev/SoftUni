num_one = int(input())
num_two = int(input())
operator = input()

result = 0

if operator == '+':
    result = num_one + num_two
    if result % 2 == 0:
        print(f'{num_one} {operator} {num_two} = {result} - even')
    else:
        print(f'{num_one} {operator} {num_two} = {result} - odd')
elif operator == '-':
    result = num_one - num_two
    if result % 2 == 0:
        print(f'{num_one} {operator} {num_two} = {result} - even')
    else:
        print(f'{num_one} {operator} {num_two} = {result} - odd')
elif operator == '*':
    result = num_one * num_two
    if result % 2 == 0:
        print(f'{num_one} {operator} {num_two} = {result} - even')
    else:
        print(f'{num_one} {operator} {num_two} = {result} - odd')
elif operator == '/':
    if num_two != 0:
        result = num_one / num_two
        print(f'{num_one} {operator} {num_two} = {result:.2f}')
    else:
        print(f'Cannot divide {num_one} by zero')
elif operator == '%':
    if num_two != 0:
        result = num_one % num_two
        print(f'{num_one} {operator} {num_two} = {result}')
    else:
        print(f'Cannot divide {num_one} by zero')