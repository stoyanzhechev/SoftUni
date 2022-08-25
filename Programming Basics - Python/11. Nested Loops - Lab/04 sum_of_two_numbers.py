interval_start = int(input())
interval_end = int(input())
magic_number = int(input())

counter = 0
combination_is_found = False

for num_1 in range(interval_start, interval_end + 1):
    for num_2 in range(interval_start, interval_end + 1):
        result = num_1 + num_2
        counter += 1
        if result == magic_number:
            combination_is_found = True
            break
    if combination_is_found: #if combination_is_found == True
        break
if combination_is_found: #if combination_is_found == True
    print(f'Combination N:{counter} ({num_1} + {num_2} = {magic_number})')
else:
    print(f'{counter} combinations - neither equals {magic_number}')


