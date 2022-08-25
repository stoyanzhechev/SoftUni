destination = input()
reservation_dates = input()
night_count = int(input())

price_per_night = 0

if destination == 'France':
    if reservation_dates == '21-23':
        price_per_night = 30
    elif reservation_dates == '24-27':
        price_per_night = 35
    elif reservation_dates == '28-31':
        price_per_night = 40
elif destination == 'Italy':
    if reservation_dates == '21-23':
        price_per_night = 28
    elif reservation_dates == '24-27':
        price_per_night = 32
    elif reservation_dates == '28-31':
        price_per_night = 39
elif destination == 'Germany':
    if reservation_dates == '21-23':
        price_per_night = 32
    elif reservation_dates == '24-27':
        price_per_night = 37
    elif reservation_dates == '28-31':
        price_per_night = 43

total_cost = price_per_night * night_count

print(f'Easter trip to {destination} : {total_cost:.2f} leva.')
