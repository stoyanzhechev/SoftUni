sums_list = input().split(', ')
beggars_count = int(input())
final_list = []
index_counter = 0
sums_list_as_digits = []

for element in sums_list:
    sums_list_as_digits.append(int(element))
while index_counter < beggars_count:
    sum_current_beggar = 0
    for current_index in range(index_counter, len(sums_list_as_digits), beggars_count):
        sum_current_beggar += sums_list_as_digits[current_index]
    index_counter += 1
    final_list.append(sum_current_beggar)

print(final_list)
