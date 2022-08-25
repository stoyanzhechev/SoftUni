available_space = float(input())

suitcases_counter = 0
total_space_taken = 0
command = input()

while command != 'End':
    suitcase_volume = float(command)
    suitcases_counter += 1
    if suitcases_counter % 3 == 0:
        suitcase_volume = 1.10 * suitcase_volume
    total_space_taken += suitcase_volume
    if total_space_taken > available_space:
        suitcases_counter -= 1
        print('No more space!')
        print(f'Statistic: {suitcases_counter} suitcases loaded.')
        break
    command = input()
else:
    print('Congratulations! All suitcases are loaded!')
    print(f'Statistic: {suitcases_counter} suitcases loaded.')



