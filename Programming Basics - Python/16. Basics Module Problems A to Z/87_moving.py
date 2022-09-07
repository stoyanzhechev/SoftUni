breadth = int(input())
length = int(input())
height = int(input())
total_volume = breadth * length * height

command = input()

while command != 'Done':
    current_box_count = int(command)
    total_volume -= current_box_count

    if total_volume <= 0:
        break

    command = input()

if total_volume <= 0:
    print(f"No more free space! You need {abs(total_volume)} Cubic meters more.")
if command == 'Done':
    print(f"{total_volume} Cubic meters left.")