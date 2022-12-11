import re

input_string = input()
searched_word = input()
searched_pattern = fr'\b{searched_word}\b'
matches = re.findall(searched_pattern, input_string, flags=re.IGNORECASE)
print(len(matches))