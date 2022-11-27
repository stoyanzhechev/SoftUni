import re

input_string = input()
searched_pattern = r'\b_[A-Za-z0-9]+\b'
result = re.findall(searched_pattern, input_string)
result_list = []
for element in result:
    element = element.split('_')
    result_list.append(element[1])

print(','.join(result_list))
