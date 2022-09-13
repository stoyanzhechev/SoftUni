beverage = input()
sugar = input()
beverage_count = int(input())

price = 0

if beverage == 'Espresso':
    if sugar == 'Without':
        price = 0.90
    elif sugar == 'Normal':
        price = 1.00
    elif sugar == 'Extra':
        price = 1.20
elif beverage == 'Cappuccino':
    if sugar == 'Without':
        price = 1.00
    elif sugar == 'Normal':
        price = 1.20
    elif sugar == 'Extra':
        price = 1.60
elif beverage == 'Tea':
    if sugar == 'Without':
        price = 0.50
    elif sugar == 'Normal':
        price = 0.60
    elif sugar == 'Extra':
        price = 0.70

total_price = beverage_count * price

if sugar == 'Without':
    total_price *= 0.65
if beverage == 'Espresso' and beverage_count >= 5:
    total_price *= 0.75
if total_price > 15.00:
    total_price *= 0.80

print(f"You bought {beverage_count} cups of {beverage} for {total_price:.2f} lv.")