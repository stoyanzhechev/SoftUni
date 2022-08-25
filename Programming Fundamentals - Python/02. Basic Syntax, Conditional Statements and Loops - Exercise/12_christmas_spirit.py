decorations_quantity = int(input())
days_till_xmas = int(input())

days_counter = 0
xmas_mood = 0
total_cost = 0

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

for days in range(days_till_xmas):
    days_counter += 1
    if days_counter % 11 == 0:
        decorations_quantity += 2
    if days_counter % 2 == 0:
        total_cost += decorations_quantity * ornament_set_price
        xmas_mood += 5
    if days_counter % 3 == 0:
        total_cost += decorations_quantity * 8
        xmas_mood += 13
    if days_counter % 5 == 0:
        total_cost += decorations_quantity * 15
        xmas_mood += 17
        if days_counter % 3 == days_counter % 5:
            xmas_mood += 30
    if days_counter % 10 == 0:
        xmas_mood -= 20
        total_cost += tree_skirt_price + tree_garland_price + tree_lights_price
if days_till_xmas % 10 == 0:
    xmas_mood -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {xmas_mood}")

