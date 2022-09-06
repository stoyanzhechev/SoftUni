initial_number = int(input())
numbers_sum = 0


while True:
    current_number = int(input())
    numbers_sum += current_number

    if numbers_sum >= initial_number:
        print(numbers_sum)
        break