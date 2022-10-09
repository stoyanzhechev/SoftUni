initial_list = input().split()
absolute_values_list = []

for element in initial_list:
    current_number = abs(float(element))
    absolute_values_list.append(current_number)

print(absolute_values_list)