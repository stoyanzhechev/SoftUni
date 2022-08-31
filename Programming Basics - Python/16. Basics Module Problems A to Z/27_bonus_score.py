initial_number = int(input())

total_points = initial_number

if initial_number <= 100:
    total_points += 5
elif initial_number > 1000:
    total_points *= 1.10
elif initial_number > 100:
    total_points *= 1.20

if initial_number % 2 == 0:
    total_points += 1

if initial_number % 10 == 5:
    total_points += 2

bonus_points = total_points - initial_number

print(bonus_points)
print(total_points)