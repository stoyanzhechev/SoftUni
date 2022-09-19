number_count = int(input())

for i in range(number_count):
    current_number = int(input())
    if current_number % 2 != 0:
        print(f'{current_number} is odd!')
        break
else:
    print('All numbers are even.')