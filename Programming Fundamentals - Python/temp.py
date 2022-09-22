decorations_quantity = int(input())
days_left = int(input())

days_counter = 0
total_spirit = 0
total_cost = 0

for day in range(days_left):
    days_counter += 1
    days_left -= 1
    if days_counter % 11 == 0:
        decorations_quantity += 2
    if days_counter % 2 == 0:
        total_cost += decorations_quantity * 2
        total_spirit += 5
    if days_counter % 3 == 0:
        total_cost += decorations_quantity * 8
        total_spirit += 13
    if days_counter % 5 == 0:
        total_cost += decorations_quantity * 15
        total_spirit += 17
        if days_counter % 3 == 0:
            total_spirit += 30
    if days_counter % 10 == 0:
        total_spirit -= 20
        total_cost += 23
        if days_left == 0:
            total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
