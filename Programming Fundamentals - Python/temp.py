factor = int(input())
count = int(input())
output_list = []

for i in range(1, count + 1):
    current_number = i * factor
    output_list.append(current_number)

print(output_list)