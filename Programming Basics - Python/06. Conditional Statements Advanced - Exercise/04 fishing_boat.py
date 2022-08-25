budget = int(input())
season = input()
people_count = int(input())

price = 0
discount = 0
extra_discount = 0

if season == 'Spring':
    price = 3000
elif season == 'Summer' or season == 'Autumn':
    price = 4200
elif season == 'Winter':
    price = 2600

if people_count <= 6:
    discount = 10
elif 6 < people_count <= 11:
    discount = 15
else:
    discount = 25

total_cost = price * (100 - discount) / 100

if season != 'Autumn' and people_count % 2 == 0:
    extra_discount = 5
else:
    extra_discount = 0

grand_total_cost = total_cost * (100 - extra_discount) / 100

diff = abs(grand_total_cost - budget)

if grand_total_cost <= budget:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')
