numbers_list = input().split()
opposite_numbers_list = []

for element in numbers_list:
    current_number = -int(element)
    opposite_numbers_list.append(current_number)

print(opposite_numbers_list)
