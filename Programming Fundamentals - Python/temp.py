nylon_quantity = int(input())
paint_quantity = int(input())
detergent_quantity = int(input())
hours_needed = int(input())

nylon_price = 1.50
paint_price = 14.50
detergent_price = 5.00
plastic_bags_price = 0.40

nylon_cost = (nylon_quantity + 2) * nylon_price
paint_cost = (paint_quantity * paint_price) * 1.10
detergent_cost = detergent_quantity * detergent_price

total_cost = nylon_cost + paint_cost + detergent_cost + plastic_bags_price
labor_price_per_hour = total_cost * 0.30
total_labor_cost = hours_needed * labor_price_per_hour

grand_total_cost = total_cost + total_labor_cost

print(grand_total_cost)