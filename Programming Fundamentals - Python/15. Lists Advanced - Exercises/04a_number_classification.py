initial_list = input().split(', ')
positive_list = []
negative_list = []
even_list = []
odd_list = []

for number in initial_list:
    current_number = int(number)
    if current_number % 2 == 0 or current_number == 0:
        even_list.append(current_number)
    else:
        odd_list.append(current_number)

for num in initial_list:
    current_num = int(num)
    if current_num >= 0:
        positive_list.append(current_num)
    else:
        negative_list.append(current_num)

print(f"Positive: {', '.join(str(number) for number in positive_list)}")
print(f"Negative: {', '.join(str(number) for number in negative_list)}")
print(f"Even: {', '.join(str(number) for number in even_list)}")
print(f"Odd: {', '.join(str(number) for number in odd_list)}")



