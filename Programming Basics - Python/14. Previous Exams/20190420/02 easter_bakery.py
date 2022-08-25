flour_cost_kg = float(input())
flour_weight_kg = float(input())
sugar_weight_kg = float(input())
eggs_count = int(input())
yeast_packs = int(input())

sugar_cost_kg = flour_cost_kg * 0.75
eggs_cost = flour_cost_kg * 1.10
yeast_cost = sugar_cost_kg * 0.20

flour_total_cost = flour_cost_kg * flour_weight_kg
sugar_total_cost = sugar_cost_kg * sugar_weight_kg
eggs_total_cost = eggs_cost * eggs_count
yeast_total_cost = yeast_cost * yeast_packs

grand_total_cost = flour_total_cost + sugar_total_cost + eggs_total_cost + yeast_total_cost

print(f'{grand_total_cost:.2f}')