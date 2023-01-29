dog_food_count = int(input())
cat_food_count = int(input())

dog_food_price = 2.50
cat_food_price = 4

dog_food_total_price = dog_food_count * dog_food_price
cat_food_total_price = cat_food_count * cat_food_price
total_price = dog_food_total_price + cat_food_total_price

print(f"{total_price} lv.")