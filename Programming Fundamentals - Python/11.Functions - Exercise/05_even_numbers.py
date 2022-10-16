def is_even(number):
    if int(number) % 2 == 0:
        return True
    return False


numbers = input().split()
filtered_number = []
for current_number in numbers:
    if is_even(current_number):
        filtered_number.append(int(current_number))
print(filtered_number)
