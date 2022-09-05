command = input()
total_money = 0

while command != 'NoMoreMoney':
    command = float(command)
    if command >= 0:
        print(f'Increase: {command:.2f}')
        total_money += command
    else:
        print('Invalid operation!')
        break
    command = input()
print(f'Total: {total_money:.2f}')