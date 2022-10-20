factor = int(input())
count = int(input())

result_list = []
current_number = 0

for number in range(count):
    current_number += factor
    result_list.append(current_number)

print(result_list)