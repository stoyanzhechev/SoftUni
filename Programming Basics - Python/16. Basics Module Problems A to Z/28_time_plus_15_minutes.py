hours = int(input())
minutes = int(input())

total_minutes = hours * 60 + minutes + 15

new_hours = total_minutes // 60
new_minutes = total_minutes % 60

if new_hours > 23:
    new_hours -= 24

if new_minutes < 10:
    print(f'{new_hours}:0{new_minutes}')
else:
    print(f'{new_hours}:{new_minutes}')
