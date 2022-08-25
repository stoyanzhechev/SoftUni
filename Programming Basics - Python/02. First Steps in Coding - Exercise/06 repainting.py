plastics = int(input())
paint = int(input())
thinner = int(input())
work_hours = int(input())

plastics_cost = (plastics + 2) * 1.50
paint_cost = (paint * 1.1) * 14.5
thinner_cost = thinner * 5.00
bags_cost = 0.40

materials_cost = plastics_cost + paint_cost + thinner_cost + bags_cost
labor_cost = (materials_cost * 0.30) * work_hours

total_cost = materials_cost + labor_cost

print(total_cost)