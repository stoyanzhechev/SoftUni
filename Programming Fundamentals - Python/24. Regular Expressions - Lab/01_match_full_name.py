import re

input_text = input()
search_pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
result = re.findall(search_pattern, input_text)

print(' '.join(result))
