hour = 0
minute = 0

total_minutes = 60 * hour + minute
total_mins = 0

for current_min in range(1, 1441):
    total_mins += 1
    if total_minutes % 60 == 0:
        hour += 1
        total_mins -= 60

    if hour == 24:
        break

    print(f'{hour} : {total_mins}')