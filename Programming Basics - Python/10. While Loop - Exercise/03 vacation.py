vacation_cost = float(input())
saved_money = float(input())

days_count = 0
spending_days_count = 0
command = ''

while saved_money < vacation_cost and spending_days_count < 5:
    command = input()
    daily_amount = float(input())
    days_count += 1
    if command == "spend":
        saved_money -= daily_amount
        spending_days_count += 1
        if saved_money < 0:
            saved_money = 0
    elif command == 'save':
        saved_money += daily_amount
        spending_days_count = 0

if spending_days_count == 5:
    print("You can't save the money.")
    print(f'{days_count}')

if saved_money >= vacation_cost:
    print(f'You saved the money for {days_count} days.')
