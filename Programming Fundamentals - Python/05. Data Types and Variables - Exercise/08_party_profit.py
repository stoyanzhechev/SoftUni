group_size = int(input())
days_count = int(input())

total_coins = 0

for days in range(1, days_count + 1):
    if days % 10 == 0:
        group_size -= 2
    if days % 15 == 0:
        group_size += 5
    total_coins += 50 - group_size * 2
    if days % 3 == 0:
        total_coins -= group_size * 3
    if days % 5 == 0:
        total_coins += group_size * 20
        if days % 3 == 0:
            total_coins -= group_size * 2

profit_per_person = total_coins // group_size

print(f"{group_size} companions received {profit_per_person} coins each.")
