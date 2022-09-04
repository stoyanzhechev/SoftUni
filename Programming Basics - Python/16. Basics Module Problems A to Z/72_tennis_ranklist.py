contests_count = int(input())
starting_points = int(input())

total_points = starting_points
contests_won = 0

for contest in range(contests_count):
    contest_stage = input()
    if contest_stage == 'W':
        contests_won += 1
        total_points += 2000
    elif contest_stage == 'F':
        total_points += 1200
    elif contest_stage == 'SF':
        total_points += 720

average_points_per_contest = (total_points - starting_points) // contests_count
win_percentage = contests_won / contests_count * 100

print(f'Final points: {total_points}')
print(f'Average points: {average_points_per_contest}')
print(f'{win_percentage:.2f}%')

