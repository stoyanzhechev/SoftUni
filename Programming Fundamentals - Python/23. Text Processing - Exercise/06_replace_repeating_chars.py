input_string = input()
final_string = ''
last_letter = ''

for current_letter in input_string:
    if current_letter != last_letter:
        final_string += current_letter
        last_letter = current_letter

print(final_string)