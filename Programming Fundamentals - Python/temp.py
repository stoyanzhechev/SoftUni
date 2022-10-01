lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_total_price = (lost_fights_count // 2) * helmet_price
sword_total_price = (lost_fights_count // 3) * sword_price
shield_total_price = (lost_fights_count // 6) * shield_price
armor_total_price = (lost_fights_count // 12) * armor_price

total_expenses = helmet_total_price + sword_total_price + shield_total_price + armor_total_price

print(f"Gladiator expenses: {total_expenses:.2f} aureus")