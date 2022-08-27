n = int(input())

positive_counter = 0
negative_sum = 0
positive_numbers_list = []
negative_numbers_list = []

for number in range(n):
    current_number = int(input())
    if current_number >= 0:
        positive_numbers_list.append(current_number)
        positive_counter += 1
    else:
        negative_numbers_list.append(current_number)
        negative_sum += current_number

print(positive_numbers_list)
print(negative_numbers_list)
print(f'Count of positives: {positive_counter} \nSum of negatives: {negative_sum}')
