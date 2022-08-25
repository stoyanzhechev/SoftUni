nominee_name = input()
academy_points = float(input())
jury_count = int(input())

current_points = academy_points

for i in range(1, jury_count + 1):
    actor_name = input()
    actor_points = float(input())

    current_points += len(actor_name) * actor_points / 2

    if current_points > 1250.5:
        print(f"Congratulations, {nominee_name} got a nominee for leading role with {current_points:.1f}!")
        break
else:
    diff = abs(1250.5 - current_points)
    print(f'Sorry, {nominee_name} you need {diff:.1f} more!')

