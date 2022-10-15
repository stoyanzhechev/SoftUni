first_string = input().split(', ')
second_string = input().split(', ')
new_string = []
for first_word in first_string:
    for second_word in second_string:
        if first_word in second_word:
            new_string.append(first_word)
            break
print(new_string)

