budget = float(input())
flour_price_kg = float(input())
eggs_price_pack = flour_price_kg * 0.75
milk_price_l = flour_price_kg * 1.25
milk_price_ml = milk_price_l / 4

colored_eggs = 0
loaf_count = 0

while budget > (flour_price_kg + eggs_price_pack + milk_price_ml):
    budget -= (flour_price_kg + eggs_price_pack + milk_price_ml)
    loaf_count += 1
    colored_eggs += 3
    if loaf_count % 3 == 0:
        colored_eggs -= (loaf_count - 2)

print(f"You made {loaf_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
