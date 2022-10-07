factor = int(input())
count = int(input())
list_of_numbers = []

for i in range(1, count + 1):
    current_number = factor * i
    list_of_numbers.append(current_number)

print(list_of_numbers)
