annual_tax = int(input())

sneakers_price = annual_tax * 0.60
suit_price = sneakers_price * 0.80
ball_price = suit_price / 4
accessories_price = ball_price / 5

total_annual_cost = annual_tax + sneakers_price + suit_price + \
    ball_price + accessories_price

print(total_annual_cost)