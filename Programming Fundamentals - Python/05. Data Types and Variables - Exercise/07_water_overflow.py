number_of_pours = int(input())
tank_capacity = 255
filled_capacity = 0

for i in range(1, number_of_pours + 1):
    current_pour = int(input())
    if filled_capacity > (tank_capacity - current_pour):
        filled_capacity += 0
        print('Insufficient capacity!')
        continue
    else:
        filled_capacity += current_pour

print(filled_capacity)