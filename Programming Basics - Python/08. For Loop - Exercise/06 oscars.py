actor_name = input()
initial_points = float(input())
jury_count = int(input())

total_points = initial_points

for i in range(1, jury_count + 1):
    name = input()
    points = float(input())
    current_points = (len(name) * points) / 2
    total_points = total_points + current_points

    if total_points >= 1250.5:
        break

if total_points < 1250.5:
    diff = 1250.5 - total_points
    print(f'Sorry, {actor_name} you need {diff:.1f} more!')
else:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')

