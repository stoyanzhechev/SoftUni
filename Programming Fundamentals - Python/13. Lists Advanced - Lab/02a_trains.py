wagons_count = int(input())
command = input()
result_list = [0] * wagons_count

while command != 'End':
    current_command = command.split(' ')
    if current_command[0] == 'add':
        result_list[-1] += int(current_command[1])
    elif current_command[0] == 'insert':
        result_list[int(current_command[1])] += int(current_command[2])
    elif current_command[0] == 'leave':
        result_list[int(current_command[1])] -= int(current_command[2])

    command = input()

print(result_list)


