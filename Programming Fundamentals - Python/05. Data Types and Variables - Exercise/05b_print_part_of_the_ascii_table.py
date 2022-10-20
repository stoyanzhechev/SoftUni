start_character = int(input())
end_character = int(input())

for char in range(start_character, end_character + 1):
    print(chr(char), end=' ')