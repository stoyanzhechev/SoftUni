plastic_needed = int(input())
paint_needed = int(input())
solvent_quantity = int(input())
working_hours = int(input())

plastic_price = 1.50
paint_price = 14.50
solvent_price = 5.00
plastic_bags = 0.40

plastic_needed += 2
paint_needed *= 1.1

total_equipment_cost = plastic_needed * plastic_price + paint_needed * paint_price + \
    solvent_quantity * solvent_price + plastic_bags
labor_cost = total_equipment_cost * working_hours * 0.30

grand_total_cost = total_equipment_cost + labor_cost

print(grand_total_cost)


