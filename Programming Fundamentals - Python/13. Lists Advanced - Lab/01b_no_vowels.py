input_string = input()
vowels_list = ['a', 'o', 'u', 'e', 'i']
result = []
for char in input_string:
    if char.lower() not in vowels_list:
        result.append(char)
print(''.join(result))