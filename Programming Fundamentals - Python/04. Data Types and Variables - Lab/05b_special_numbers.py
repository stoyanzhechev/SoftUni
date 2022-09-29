number = int(input())

for i in range(1, number + 1):
    digits_sum = 0
    if i % 10 != 0:
        digits_sum += i % 10
    if i > 10:
        digits_sum += int(i // 10)

    is_special = digits_sum == 5 or digits_sum == 7 or digits_sum == 11

    if is_special:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')

