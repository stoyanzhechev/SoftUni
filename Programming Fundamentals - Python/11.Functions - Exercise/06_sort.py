initial_list = input().split()
sorted_list = []

for element in initial_list:
    number = int(element)
    sorted_list.append(number)
sorted_list = sorted(sorted_list)
print(sorted_list)