initial_list = input().split()
absolute_values_list = []

for number in initial_list:
    absolute_values_list.append(abs(float(number)))

print(absolute_values_list)
