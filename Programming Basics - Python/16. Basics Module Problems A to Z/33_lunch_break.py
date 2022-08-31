from math import ceil

movie_name = input()
movie_duration = int(input())
break_duration = int(input())

lunch_duration = break_duration / 8
rest_duration = break_duration / 4

total_duration = movie_duration + lunch_duration + rest_duration
diff = abs(total_duration - break_duration)

if break_duration >= total_duration:
    print(f"You have enough time to watch {movie_name} and left with {ceil(diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {ceil(diff)} more minutes.")