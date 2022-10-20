initial_list = input().split()
numbers_to_remove = int(input())
initial_list_as_digits = []
final_list = []

for element in initial_list:
    current_number = int(element)
    initial_list_as_digits.append(current_number)

for number in range(numbers_to_remove):
    initial_list_as_digits.remove(min(initial_list_as_digits))

for final_number in initial_list_as_digits:
    final_element = str(final_number)
    final_list.append(final_element)

print(', '.join(final_list))
