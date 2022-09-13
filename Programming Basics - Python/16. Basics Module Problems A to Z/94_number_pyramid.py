initial_number = int(input())

for row in range(1, initial_number + 1):
    for column in range(1, initial_number + 1):
        current_number = 1
        is_current_number_bigger_than_initial_number = False
        if current_number > current_number:
            is_current_number_bigger_than_initial_number = True
            break
        print(f'{current_number} ', end='')
        current_number += 1
    if is_current_number_bigger_than_initial_number:
        break
    print()



