destination = input()


while destination != 'End':
    cost = float(input())
    money_saved = 0
    while money_saved < cost:
        current_money = float(input())
        money_saved += current_money
    print(f'Going to {destination}!')

    destination = input()