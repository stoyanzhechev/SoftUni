vacation_cost = float(input())
available_budget = float(input())
days_count = 0
total_spending_days = 0
money_saved = False

while available_budget < vacation_cost:
    command = input()
    daily_amount = float(input())
    days_count += 1

    if command == 'save':
        available_budget += daily_amount
        total_spending_days = 0
    elif command == 'spend':
        total_spending_days += 1
        if daily_amount > available_budget:
            available_budget = 0
        else:
            available_budget -= daily_amount
        if total_spending_days == 5:
            break

    if available_budget >= vacation_cost:
        money_saved = True

if money_saved:
    print(f"You saved the money for {days_count} days.")
else:
    print(f"You can't save the money.")
    print(f"{days_count}")
