budget = int(input())
season = input()
fishermen_count = int(input())

boat_hire = 0
discount = 0
extra_discount = 0

if season == 'Spring':
    boat_hire = 3000
    if fishermen_count <= 6:
        discount = 10
    elif fishermen_count <= 11:
        discount = 15
    else:
        discount = 25
elif season == 'Summer' or season == 'Autumn':
    boat_hire = 4200
    if fishermen_count <= 6:
        discount = 10
    elif fishermen_count <= 11:
        discount = 15
    else:
        discount = 25
elif season == 'Winter':
    boat_hire = 2600
    if fishermen_count <= 6:
        discount = 10
    elif fishermen_count <= 11:
        discount = 15
    else:
        discount = 25

initially_discounted_price = boat_hire * ((100 - discount) / 100)

if fishermen_count % 2 == 0 and season != 'Autumn':
    extra_discount = 5
else:
    extra_discount = 0

total_discounted_price = initially_discounted_price * ((100 - extra_discount) / 100)
diff = abs(budget - total_discounted_price)

if budget >= total_discounted_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
