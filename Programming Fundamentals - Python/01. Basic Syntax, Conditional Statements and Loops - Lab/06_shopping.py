budget = int(input())

command = input()
while command != 'End':
    item_price = int(command)
    budget -= item_price
    if budget < 0:
        print('You went in overdraft!')
        break
    command = input()
else:
    print('You bought everything needed.')

