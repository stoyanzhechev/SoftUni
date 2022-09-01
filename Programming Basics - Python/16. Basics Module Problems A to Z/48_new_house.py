flower_type = input()
flower_count = int(input())
budget = int(input())

flower_price = 0
discount = 0

if flower_type == 'Roses':
    flower_price = 5.00
    if flower_count > 80:
        discount = 10
elif flower_type == 'Dahlias':
    flower_price = 3.80
    if flower_count > 90:
        discount = 15
elif flower_type == 'Tulips':
    flower_price = 2.80
    if flower_count > 80:
        discount = 15
elif flower_type == 'Narcissus':
    flower_price = 3.00
    if flower_count < 120:
        discount = -15
elif flower_type == 'Gladiolus':
    flower_price = 2.50
    if flower_count < 80:
        discount = -20

initial_total_cost = flower_price * flower_count
discounted_total_price = initial_total_cost - initial_total_cost * discount / 100
diff = abs(budget - discounted_total_price)

if budget >= discounted_total_price:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")