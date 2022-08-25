movie_budget = float(input())
statists_count = int(input())
suit_price_unit = float(input())

suits_price = statists_count * suit_price_unit
decors_price = movie_budget * 0.10

if statists_count > 150:
    suits_price = suits_price * 0.90

total_cost = decors_price + suits_price

diff = abs(total_cost - movie_budget)

if total_cost > movie_budget:
    print('Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')