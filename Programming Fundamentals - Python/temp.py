coffee_list = input().split()
commands_number = int(input())

for commands in range(0, commands_number):
    command = input().split()
    command_action = command[0]
    if command_action == 'Include':
        coffee_list.append(command[1])
    elif command_action == 'Remove':
        number_of_coffees_to_remove = int(command[2])
        if command[1] == 'first':
            del coffee_list[:number_of_coffees_to_remove]
        elif command[1] == 'last':
            del coffee_list[len(coffee_list) - number_of_coffees_to_remove:]
    elif command_action == 'Prefer':
        first_coffee_index = int(command[1])
        second_coffee_index = int(command[2])
        if first_coffee_index < len(coffee_list) and second_coffee_index < len(coffee_list):
            coffee_list[first_coffee_index], coffee_list[second_coffee_index] = \
            coffee_list[second_coffee_index], coffee_list[first_coffee_index]
    elif command_action == 'Reverse':
        coffee_list.reverse()

print('Coffees:')
print(' '.join(coffee_list))