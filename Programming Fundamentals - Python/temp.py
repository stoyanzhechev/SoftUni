number_of_snowballs = int(input())
best_snowball_score = 0
best_weight = 0
best_time = 0
best_quality = 0

for current_snowball in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    current_snowball_score = (snowball_weight / snowball_time) ** snowball_quality
    if current_snowball_score > best_snowball_score:
        best_weight = snowball_weight
        best_time = snowball_time
        best_quality = snowball_quality
        best_snowball_score = current_snowball_score
print(f"{best_weight} : {best_time} = {int(best_snowball_score)} ({best_quality})")
