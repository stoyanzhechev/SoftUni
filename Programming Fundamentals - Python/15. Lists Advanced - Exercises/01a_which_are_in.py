first_string = input().split(', ')
second_string = input().split(', ')
new_list = []
for first_word in first_string:
    for second_word in second_string:
        if first_word in second_word and not first_word in new_list:
            new_list.append(first_word)
print(new_list)
