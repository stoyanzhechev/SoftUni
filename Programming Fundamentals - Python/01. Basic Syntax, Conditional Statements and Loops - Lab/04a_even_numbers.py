number_count = int(input())
odd_number = False

for i in range(number_count):
    current_number = int(input())
    if current_number % 2 != 0:
        odd_number = True
        break
if odd_number:
    print(f'{current_number} is odd!')
else:
    print('All numbers are even.')