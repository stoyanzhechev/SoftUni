from sys import maxsize

number_count = int(input())

total_sum = 0
max_num = -maxsize
for num in range(number_count):
    current_number = int(input())
    total_sum += current_number

    if current_number > max_num:
        max_num = current_number

if max_num == total_sum - max_num:
    print(f'Yes \nSum = {max_num}')
else:
    diff = abs(max_num - (total_sum - max_num))
    print(f'No \nDiff = {diff}')
