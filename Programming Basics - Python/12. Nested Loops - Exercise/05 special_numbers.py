number = int(input())

for current_num in range(1111, 10000):
    current_num_is_special = True
    current_num_as_str = str(current_num)
    for current_digit in current_num_as_str:
        if int(current_digit) == 0 or number % int(current_digit) != 0:
            current_num_is_special = False
            break
        else:
            current_num_is_special = True
    if current_num_is_special:
        print(current_num_as_str, end=' ')
