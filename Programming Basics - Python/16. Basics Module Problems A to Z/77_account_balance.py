command = input()
total_money_saved = 0

while command != 'NoMoreMoney':
    increase = float(command)
    if increase >= 0:
        total_money_saved += increase
        print(f'Increase: {increase:.2f}')
    else:
        print('Invalid operation!')
        break
    command = input()

print(f'Total: {total_money_saved:.2f}')


