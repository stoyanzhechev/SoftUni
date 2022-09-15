from math import ceil

wall_height = int(input())
wall_breadth = int(input())
void_area_percentage = int(input())

total_area_for_painting = wall_breadth * wall_height * 4
grand_total_area = ceil(total_area_for_painting * (100 - void_area_percentage) / 100)
all_walls_painted = False

command = input()
while command != 'Tired!':
    paint_liters = int(command)
    grand_total_area -= paint_liters

    if grand_total_area <= 0:
        all_walls_painted = True
        break

    command = input()

if not all_walls_painted:
    print(f"{grand_total_area} quadratic m left.")
else:
    diff = abs(grand_total_area)
    if grand_total_area < 0:
        print(f"All walls are painted and you have {diff} l paint left!")
    else:
        print("All walls are painted! Great job, Pesho!")



