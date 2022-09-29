number = int(input())

for n in range(1, number + 1):
    working_num = n
    digit_sum = 0
    while working_num > 0:
        digit_sum += working_num % 10
        working_num = int(working_num / 10)

    is_special = digit_sum == 5 or digit_sum == 7 or digit_sum == 11
    print(f'{n} -> {is_special}')

