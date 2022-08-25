from math import ceil

guest_count = int(input())
budget = int(input())

cakes_count = ceil(guest_count / 3)
eggs_count = guest_count * 2

total_cakes_cost = cakes_count * 4
total_eggs_cost = eggs_count * 0.45

grand_total_cost = total_cakes_cost + total_eggs_cost
diff = abs(budget - grand_total_cost)

if budget >= grand_total_cost:
    print(f"Lyubo bought {cakes_count} Easter bread and {eggs_count} eggs.")
    print(f"He has {diff:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")