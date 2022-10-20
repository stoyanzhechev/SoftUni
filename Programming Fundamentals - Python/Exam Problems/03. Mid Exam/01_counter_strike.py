total_energy = int(input())
command = input()
win_counter = 0

while command != 'End of battle':
    distance = int(command)
    if total_energy >= distance:
        total_energy -= distance
        win_counter += 1
        if win_counter % 3 == 0:
            total_energy += win_counter
    else:
        print(f'Not enough energy! Game ends with {win_counter} won battles and {total_energy} energy')
        break
    command = input()
else:
    print(f'Won battles: {win_counter}. Energy left: {total_energy}')

