total_money = 0
command = input()

while command != 'NoMoreMoney':
    increase = float(command)
    if increase >= 0:
        print(f'Increase: {increase:.2f}')
        total_money += increase
    else:
        print('Invalid operation!')
        total_money += 0
        break
    command = input()

print(f'Total: {total_money:.2f}')

