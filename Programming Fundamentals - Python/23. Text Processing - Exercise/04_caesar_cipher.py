input_string = input()
encrypted_string = ''

for character in input_string:
    new_symbol = chr(ord(character) + 3)
    encrypted_string += new_symbol

print(encrypted_string)