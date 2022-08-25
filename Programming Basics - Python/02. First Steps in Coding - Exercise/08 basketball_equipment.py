annual_cost = int(input())

sneakers_cost = annual_cost * 0.60
suit_cost = sneakers_cost * 0.80
ball_cost = suit_cost / 4
accessories_cost = ball_cost / 5

equipment_cost = sneakers_cost + suit_cost + ball_cost + accessories_cost

total_annual_cost = annual_cost + equipment_cost

print(total_annual_cost)
