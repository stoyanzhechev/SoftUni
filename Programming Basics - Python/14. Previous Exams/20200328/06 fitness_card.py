budget = float(input())
gender = input()
age = int(input())
sport = input()

monthly_cost = 0

if gender == 'm':
    if sport == 'Gym':
        monthly_cost = 42
    elif sport == 'Boxing':
        monthly_cost = 41
    elif sport == 'Yoga':
        monthly_cost = 45
    elif sport == 'Zumba':
        monthly_cost = 34
    elif sport == 'Dances':
        monthly_cost = 51
    elif sport == 'Pilates':
        monthly_cost = 39
elif gender == 'f':
    if sport == 'Gym':
        monthly_cost = 35
    elif sport == 'Boxing':
        monthly_cost = 37
    elif sport == 'Yoga':
        monthly_cost = 42
    elif sport == 'Zumba':
        monthly_cost = 31
    elif sport == 'Dances':
        monthly_cost = 53
    elif sport == 'Pilates':
        monthly_cost = 37

if age <= 19:
    monthly_cost = 0.80 * monthly_cost

if budget >= monthly_cost:
    print(f'You purchased a 1 month pass for {sport}.')
else:
    diff = abs(budget - monthly_cost)
    print(f"You don't have enough money! You need ${diff:.2f} more.")