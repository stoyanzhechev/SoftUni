number_of_lines = int(input())
sum_of_chars = 0

for char in range(number_of_lines):
    char = input()
    ascii_number = ord(char)
    sum_of_chars += ascii_number

print(f'The sum equals: {sum_of_chars}')
