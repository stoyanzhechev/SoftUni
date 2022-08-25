import math

tournaments_count = int(input())
initial_points = int(input())

current_points = initial_points

win_count = 0

for i in range(1, tournaments_count + 1):
    tournament_stage = input()
    if tournament_stage == 'W':
        current_points = current_points + 2000
        win_count = win_count + 1
    elif tournament_stage == 'F':
        current_points = current_points + 1200
    elif tournament_stage == 'SF':
        current_points = current_points + 720

average_points = (current_points - initial_points) / tournaments_count

print(f'Final points: {current_points}')
print(f'Average points: {math.floor(average_points)}')

win_percentage = (win_count / tournaments_count) * 100

print(f'{win_percentage:.2f}%')

