initial_list = list(map(int, input().split()))
average_number = sum(initial_list) / len(initial_list)
interim_list = []
final_list = []
numbers_counter = 0

for i in range(len(initial_list)):
    current_number = int(initial_list[i])
    if current_number > average_number:
        interim_list.append(current_number)

for j in range(len(interim_list)):
    if numbers_counter == 5:
        break
    final_number = max(interim_list)
    interim_list.remove(final_number)
    final_list.append(final_number)
    numbers_counter += 1

if final_list == []:
    print('No')
else:
    print(' '.join([str(num) for num in final_list]))
