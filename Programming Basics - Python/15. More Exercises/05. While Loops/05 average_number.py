nums_count = int(input())

total_sum = 0

for i in range(nums_count):
    current_num = int(input())
    total_sum += current_num
    average = total_sum / nums_count
print(f'{average:.2f}')
