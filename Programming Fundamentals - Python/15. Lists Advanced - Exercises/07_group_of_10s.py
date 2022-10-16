numbers_sequence = [int(number) for number in input().split(', ')]
numbers_counter = 0
group_of_numbers = 10
while numbers_counter < len(numbers_sequence):
    collected_numbers = []
    for number in numbers_sequence:
        if group_of_numbers - 10 < number <= group_of_numbers:
            collected_numbers.append(number)
            numbers_counter += 1
    print(f"Group of {group_of_numbers}'s: {collected_numbers}")
    group_of_numbers += 10
