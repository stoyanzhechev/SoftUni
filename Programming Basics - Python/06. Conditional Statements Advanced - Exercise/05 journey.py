budget = float(input())
season = input()

destination = ''
holiday_type = ''
price = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        holiday_type = 'Camp'
        price = 0.30 * budget
    elif season == 'winter':
        holiday_type = 'Hotel'
        price = 0.70 * budget
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        holiday_type = 'Camp'
        price = 0.40 * budget
    elif season == 'winter':
        holiday_type = 'Hotel'
        price = 0.80 * budget
else:
    destination = 'Europe'
    if season == 'summer':
        holiday_type = 'Hotel'
        price = 0.90 * budget
    elif season == 'winter':
        holiday_type = 'Hotel'
        price = 0.90 * budget

print(f'Somewhere in {destination}')
print(f'{holiday_type} - {price:.2f}')
