from math import ceil

wall_height = int(input())
wall_width = int(input())
clear_walls_perrcentage = int(input())
all_is_painted = False

area_for_painting = wall_height * wall_width * 4
area_for_painting = area_for_painting * (100 - clear_walls_perrcentage) / 100
command = input()

while command != 'Tired!':
    current_litres_paint = int(command)
    area_for_painting -= current_litres_paint
    if area_for_painting <= 0:
        all_is_painted = True
        break

    command = input()

if all_is_painted:
    if area_for_painting < 0:
        print(f'All walls are painted and you have {ceil(abs(area_for_painting))} l paint left!')
    else:
        print('All walls are painted! Great job, Pesho!')
else:
    print(f'{round(area_for_painting)} quadratic m left.')