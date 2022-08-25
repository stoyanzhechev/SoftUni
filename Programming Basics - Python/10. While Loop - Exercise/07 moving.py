home_width = int(input())
home_length = int(input())
home_height = int(input())

home_volume = home_length * home_width * home_height
cartons_count = 0

input_line = input()

while input_line != 'Done':
    boxes = int(input_line)
    cartons_count += boxes

    if cartons_count >= home_volume:
        break

    input_line = input()

diff = abs(cartons_count - home_volume)

if cartons_count >= home_volume:
    print(f'No more free space! You need {diff} Cubic meters more.')
else:
    print(f'{diff} Cubic meters left.')




