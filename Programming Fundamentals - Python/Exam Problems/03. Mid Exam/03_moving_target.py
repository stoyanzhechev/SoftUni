targets_list = list(map(int, input().split()))
command = input()

while command != 'End':
    command = command.split()
    command_action = command[0]
    command_index = int(command[1])
    if command_action == 'Shoot':
        if 0 <= command_index < len(targets_list):
            command_power = int(command[2])
            targets_list[command_index] -= command_power
            if targets_list[command_index] <= 0:
                targets_list.remove(targets_list[command_index])
    elif command_action == 'Add':
        command_value = int(command[2])
        if 0 <= command_index < len(targets_list):
            targets_list.insert(command_index, command_value)
        else:
            print('Invalid placement!')
    elif command_action == 'Strike':
        command_radius = int(command[2])
        if 0 <= command_index - command_radius < len(targets_list) and 0 <= command_index + command_radius < len(targets_list):
            targets_list = [targets_list[i] for i in range(len(targets_list)) if i < command_index - command_radius or i > command_index + command_radius]
        else:
            print('Strike missed!')
    command = input()

targets_list_converted_to_string = [str(num) for num in targets_list]
print('|'.join(targets_list_converted_to_string))