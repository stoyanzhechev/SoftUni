turns_count = int(input())

total_score = 0

from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid_nums = 0

for number in range(turns_count):
    current_num = int(input())
    if 0 <= current_num <= 9:
        from_0_to_9 += 1
        total_score += current_num * 0.20
    elif 10 <= current_num <= 19:
        from_10_to_19 += 1
        total_score += current_num * 0.30
    elif 20 <= current_num <= 29:
        total_score += current_num * 0.40
        from_20_to_29 += 1
    elif 30 <= current_num <= 39:
        total_score += 50
        from_30_to_39 += 1
    elif 40 <= current_num <= 50:
        total_score += 100
        from_40_to_50 += 1
    else:
        total_score /= 2
        invalid_nums += 1

from_0_to_9_percentage = from_0_to_9 / turns_count * 100
from_10_to_19_percentage = from_10_to_19 / turns_count * 100
from_20_to_29_percentage = from_20_to_29 / turns_count * 100
from_30_to_39_percentage = from_30_to_39 / turns_count * 100
from_40_to_50_percentage = from_40_to_50 / turns_count * 100
invalid_nums_percentage = invalid_nums / turns_count * 100

print(f'{total_score:.2f}')
print(f"From 0 to 9: {from_0_to_9_percentage:.2f}%")
print(f"From 10 to 19: {from_10_to_19_percentage:.2f}%")
print(f"From 20 to 29: {from_20_to_29_percentage:.2f}%")
print(f"From 30 to 39: {from_30_to_39_percentage:.2f}%")
print(f"From 40 to 50: {from_40_to_50_percentage:.2f}%")
print(f"Invalid numbers: {invalid_nums_percentage:.2f}%")