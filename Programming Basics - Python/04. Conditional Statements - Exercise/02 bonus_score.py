# Pay specific attention to the formula on line 20 - number ending at 'x' (in this case x = 5)

points = int(input())

bonus_points = 0

if points <= 100:
    bonus_points = 5
elif points > 1000:
    bonus_points = points * 0.10
else:
    bonus_points = points * 0.20

extra_bonus = 0

if points % 2 == 0:
    extra_bonus = 1

if points % 10 == 5:
    extra_bonus = 2

total_bonus = bonus_points + extra_bonus
total_points = points + total_bonus

print(total_bonus)
print(total_points)