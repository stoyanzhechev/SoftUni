wagons_number = int(input())
wagons_list = [0] * wagons_number

while True:
    command = input()

    if command == 'End':
        break

    current_command = command.split(' ')
    first_command = current_command[0]
    if first_command == 'add':
        people_count = int(current_command[1])
        wagons_list[-1] += people_count
    elif first_command == 'insert':
        wagon_index = int(current_command[1])
        people_count = int(current_command[2])
        wagons_list[wagon_index] += people_count
    elif first_command == 'leave':
        wagon_index = int(current_command[1])
        people_count = int(current_command[2])
        wagons_list[wagon_index] -= people_count

print(wagons_list)

