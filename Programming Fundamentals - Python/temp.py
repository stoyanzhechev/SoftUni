group_size = int(input())
adventure_days = int(input())
days_counter = 0
total_coins = 0

for current_day in range(1, adventure_days + 1):
    days_counter += 1
    if days_counter % 10 == 0:
        group_size -= 2
    if days_counter % 15 == 0:
        group_size += 5
    total_coins += 50 - (group_size * 2)
    if days_counter % 3 == 0:
        total_coins -= group_size * 3
    if days_counter % 5 == 0:
        total_coins += group_size * 20
        if days_counter % 3 == 0:
            total_coins -= group_size * 2
coins_per_party_member = int(total_coins / group_size)

print(f"{group_size} companions received {coins_per_party_member} coins each.")