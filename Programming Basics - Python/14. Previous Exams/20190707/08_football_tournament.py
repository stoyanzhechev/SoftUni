team_name = input()
matches_played = int(input())

points_count = 0
win_matches = 0
draw_matches = 0
loss_matches = 0

for match in range(matches_played):
    match_result = input()
    if match_result == 'W':
        points_count += 3
        win_matches += 1
    elif match_result == 'D':
        points_count += 1
        draw_matches += 1
    elif match_result == 'L':
        points_count += 0
        loss_matches += 1

if matches_played == 0:
    print(f"{team_name} hasn't played any games during this season.")
elif matches_played > 0:
    win_rate = win_matches / matches_played * 100
    print(f"{team_name} has won {points_count} points during this season.")
    print("Total stats:")
    print(f"## W: {win_matches}")
    print(f"## D: {draw_matches}")
    print(f"## L: {loss_matches}")
    print(f"Win rate: {win_rate:.2f}%")