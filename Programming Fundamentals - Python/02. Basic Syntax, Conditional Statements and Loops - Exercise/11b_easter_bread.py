budget = float(input())
flour_price_kg = float(input())
eggs_price_pack = flour_price_kg * 0.75
milk_price_ltr = flour_price_kg * 1.25
milk_price_per_loaf = milk_price_ltr / 4
cost_per_loaf = flour_price_kg + eggs_price_pack + milk_price_per_loaf
total_loaves_count = 0
colored_eggs_count = 0

while True:
    if budget >= cost_per_loaf:
        budget -= cost_per_loaf
        total_loaves_count += 1
        colored_eggs_count += 3
        if total_loaves_count % 3 == 0:
            colored_eggs_count -= (total_loaves_count - 2)
    else:
        break

print(f"You made {total_loaves_count} loaves of Easter bread! Now you have \
{colored_eggs_count} eggs and {budget:.2f}BGN left.")
