banned_words = input().split(', ')
input_string = input()

for word in banned_words:
    while word in input_string:
        input_string = input_string.replace(word, '*' * len(word))
print(input_string)
