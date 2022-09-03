number_count = int(input())

left_sum = 0
right_sum = 0

for i in range(number_count * 2):
    current_number = int(input())
    if i < number_count:
        left_sum += current_number
    else:
        right_sum += current_number

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    diff = abs(left_sum - right_sum)
    print(f'No, diff = {diff}')
