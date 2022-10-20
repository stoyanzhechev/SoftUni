number_of_lines = int(input())

positive_numbers_list = []
negative_numbers_list = []
positive_number_count = 0
negative_numbers_sum = 0

for i in range(number_of_lines):
    current_number = int(input())
    if current_number >= 0:
        positive_number_count += 1
        positive_numbers_list.append(current_number)
    else:
        negative_numbers_list.append(current_number)
        negative_numbers_sum += current_number

print(positive_numbers_list)
print(negative_numbers_list)
print(f'Count of positives: {positive_number_count}')
print(f'Sum of negatives: {negative_numbers_sum}')

