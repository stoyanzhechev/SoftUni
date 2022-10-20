lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_expenses = 0
shield_breaks_count = 0

for current_fight in range(1, lost_fights_count + 1):
    if current_fight % 2 == 0:
        total_expenses += helmet_price
    if current_fight % 3 == 0:
        total_expenses += sword_price
        if current_fight % 2 == 0:
            shield_breaks_count += 1
            total_expenses += shield_price
            if shield_breaks_count % 2 == 0:
                total_expenses += armor_price

print(f"Gladiator expenses: {total_expenses:.2f} aureus")
