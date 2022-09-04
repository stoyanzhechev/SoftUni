initial_number = int(input())

current_number = int(input())
total_sum = 0
while True:
    total_sum += current_number

    if total_sum >= initial_number:
        break
    current_number = int(input())

print(total_sum)