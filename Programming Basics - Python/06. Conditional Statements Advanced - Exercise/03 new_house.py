flowers_type = input()
flowers_count = int(input())
budget = int(input())

price = 0

if flowers_type == 'Roses':
    price = 5.00
elif flowers_type == 'Dahlias':
    price = 3.80
elif flowers_type == 'Tulips':
    price = 2.80
elif flowers_type == 'Narcissus':
    price = 3.00
elif flowers_type == 'Gladiolus':
    price = 2.50

total_price = flowers_count * price

if flowers_type == 'Roses' and flowers_count > 80:
    total_price = 0.90 * total_price

if flowers_type == 'Dahlias' and flowers_count > 90:
    total_price = 0.85 * total_price

if flowers_type == 'Tulips' and flowers_count > 80:
    total_price = 0.85 * total_price

if flowers_type == 'Narcissus' and flowers_count < 120:
    total_price = 1.15 * total_price

if flowers_type == 'Gladiolus' and flowers_count < 80:
    total_price = 1.20 * total_price

diff = abs(total_price - budget)

if total_price <= budget:
    print(f'Hey, you have a great garden with {flowers_count} {flowers_type} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')