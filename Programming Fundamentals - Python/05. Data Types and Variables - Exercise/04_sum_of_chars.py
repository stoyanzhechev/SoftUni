characters_count = int(input())
ascii_value = 0

for character in range(characters_count):
    current_char = input()
    ascii_value += ord(current_char)

print(f'The sum equals: {ascii_value}')