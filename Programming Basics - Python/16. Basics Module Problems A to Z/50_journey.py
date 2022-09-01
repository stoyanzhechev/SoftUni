budget = float(input())
season = input()

vacation_cost = 0
vacation_destination = ''
vacation_type = ''

if budget <= 100:
    vacation_destination = 'Bulgaria'
    if season == 'summer':
        vacation_cost = budget * 0.30
        vacation_type = 'Camp'
    elif season == 'winter':
        vacation_cost = budget * 0.70
        vacation_type = 'Hotel'
elif budget <= 1000:
    vacation_destination = 'Balkans'
    if season == 'summer':
        vacation_cost = budget * 0.40
        vacation_type = 'Camp'
    elif season == 'winter':
        vacation_cost = budget * 0.80
        vacation_type = 'Hotel'
else:
    vacation_destination = 'Europe'
    vacation_type = 'Hotel'
    vacation_cost = budget * 0.90

print(f"Somewhere in {vacation_destination}")
print(f"{vacation_type} - {vacation_cost:.2f}")

