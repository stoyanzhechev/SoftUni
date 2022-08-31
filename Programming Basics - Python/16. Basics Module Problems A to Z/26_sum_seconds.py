first_player_time = int(input())
second_player_time = int(input())
third_player_time = int(input())

total_time_sec = first_player_time + second_player_time + third_player_time
total_time_min = 0

if total_time_sec // 60 > 0:
    total_time_min = total_time_sec // 60
    total_time_sec = total_time_sec % 60
    if total_time_sec < 10:
        print(f'{total_time_min}:0{total_time_sec}')
    else:
        print(f'{total_time_min}:{total_time_sec}')
else:
    if total_time_sec < 10:
        print(f'0:0{total_time_sec}')
    else:
        print(f'0:{total_time_sec}')
