import re

input_phone = input()
searched_pattern = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'
result = re.findall(searched_pattern, input_phone)

print(', '.join(result))