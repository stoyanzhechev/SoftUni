days_count = int(input())
total_food_available = float(input())

total_eaten_by_dog = 0
total_eaten_by_cat = 0
biscuits_eaten = 0
total_biscuits_eaten = 0

for days in range(1, days_count + 1):
    eaten_by_dog = int(input())
    eaten_by_cat = int(input())
    total_eaten_by_dog += eaten_by_dog
    total_eaten_by_cat += eaten_by_cat
    if days % 3 == 0:
        biscuits_eaten = (eaten_by_cat + eaten_by_dog) * 0.10
        total_biscuits_eaten += biscuits_eaten

print(f"Total eaten biscuits: {round(total_biscuits_eaten)}gr.")
eaten_food_percentage = (total_eaten_by_cat + total_eaten_by_dog) * 100 / total_food_available
print(f"{eaten_food_percentage:.2f}% of the food has been eaten.")
dog_eaten_percentage = total_eaten_by_dog * 100 / (total_eaten_by_cat + total_eaten_by_dog)
print(f"{dog_eaten_percentage:.2f}% eaten from the dog.")
cat_eaten_percentage = total_eaten_by_cat * 100 / (total_eaten_by_cat + total_eaten_by_dog)
print(f"{cat_eaten_percentage:.2f}% eaten from the cat.")

