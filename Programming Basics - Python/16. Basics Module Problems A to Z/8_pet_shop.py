dog_food_count = int(input())
cat_food_count = int(input())

dog_food_price = 2.50
cat_food_price = 4.00

total_dog_food_cost = dog_food_count * dog_food_price
total_cat_food_cost = cat_food_count * cat_food_price

total_cost = total_dog_food_cost + total_cat_food_cost

print(f'{total_cost} lv.')
