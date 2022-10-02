n = int(input())

positive_numbers_list = []
negative_numbers_list = []

for row in range(n):
    current_number = int(input())
    if current_number >= 0:
        positive_numbers_list.append(current_number)
    else:
        negative_numbers_list.append(current_number)

print(positive_numbers_list)
print(negative_numbers_list)
print(f'Count of positives: {len(positive_numbers_list)} \nSum of negatives: {sum(negative_numbers_list)}')
