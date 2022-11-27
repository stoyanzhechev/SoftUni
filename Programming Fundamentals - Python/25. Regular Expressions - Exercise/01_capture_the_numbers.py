import re

input_string = input()
while input_string:
    searched_pattern = r'[0-9]+'
    result = re.findall(searched_pattern, input_string)
    if result:
        print(' '.join(result), end=' ')
    input_string = input()

