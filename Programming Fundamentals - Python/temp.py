input_string = input().split()
text_string = ''.join(input_string)
result_dictionary = {}

for symbol in text_string:
    if symbol not in result_dictionary:
        result_dictionary[symbol] = 0
    result_dictionary[symbol] += 1
for char, occurrences in result_dictionary.items():
    print(f"{char} -> {occurrences}")


