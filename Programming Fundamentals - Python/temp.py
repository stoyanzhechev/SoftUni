initial_list = input().split(', ')
number_of_beggars = int(input())
initial_list_as_digits = []
final_list = []
index_counter = 0

for element in initial_list:
    initial_list_as_digits.append(int(element))

while index_counter < number_of_beggars:
    current_beggar_sum = 0

    for current_index in range(index_counter, len(initial_list_as_digits), number_of_beggars):
        current_beggar_sum += initial_list_as_digits[current_index]
    index_counter += 1
    final_list.append(current_beggar_sum)

print(final_list)







