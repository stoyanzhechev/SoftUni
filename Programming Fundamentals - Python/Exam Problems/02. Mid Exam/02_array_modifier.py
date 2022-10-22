array = list(map(int, input().split()))
command = input()

while command != 'end':
    current_command = command.split()
    current_command_action = current_command[0]
    if current_command_action == 'swap':
        array[int(current_command[1])], array[int(current_command[2])] = array[int(current_command[2])], array[
            int(current_command[1])]
    elif current_command_action == 'multiply':
        product = array[int(current_command[1])] * array[int(current_command[2])]
        array[int(current_command[1])] = product
    elif current_command_action == 'decrease':
        for element in range(len(array)):
            array[element] -= 1

    command = input()

print(', '.join([str(num) for num in array]))
