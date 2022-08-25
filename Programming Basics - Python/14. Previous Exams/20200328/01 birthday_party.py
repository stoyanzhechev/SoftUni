hall_rent = float(input())

cake_cost = 0.2 * hall_rent
beverages_cost = 0.55 * cake_cost
animation_cost = hall_rent / 3

total_cost = hall_rent + cake_cost + beverages_cost + animation_cost

print(f'{total_cost:.1f}')