money_list = input().split(', ')
beggars_count = int(input())
final_sums_list = []
money_list_as_digits = []
starting_index = 0

for element in money_list:
    money_list_as_digits.append(int(element))

while starting_index < beggars_count:
    current_beggar_sum = 0

    for current_index in range(starting_index, len(money_list_as_digits), beggars_count):
        current_beggar_sum += money_list_as_digits[current_index]
    final_sums_list.append(current_beggar_sum)
    starting_index += 1

print(final_sums_list)
