interval_start = int(input())
interval_end = int(input())
magic_number = int(input())
counter = 0
combination_found = False

for first_number in range(interval_start, interval_end + 1):
    for second_number in range(interval_start, interval_end + 1):
        counter += 1
        result = first_number + second_number
        if result == magic_number:
            combination_found = True
            break
    if combination_found:
        break
if combination_found:
    print(f"Combination N:{counter} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{counter} combinations - neither equals {magic_number}")
