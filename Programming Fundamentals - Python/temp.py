initial_groceries_list = input().split('!')
command = input()

while command != 'Go Shopping!':
    current_command = command.split()
    if current_command[0] == 'Urgent':
        if current_command[1] not in initial_groceries_list:
            initial_groceries_list.insert(0, current_command[1])
    elif current_command[0] == 'Unnecessary':
        if current_command[1] in initial_groceries_list:
            initial_groceries_list.remove(current_command[1])
    elif current_command[0] == 'Correct':
        old_item = current_command[1]
        new_item = current_command[2]
        if old_item in initial_groceries_list:
            old_item_index = initial_groceries_list.index(old_item)
            initial_groceries_list.pop(old_item_index)
            initial_groceries_list.insert(old_item_index, new_item)
    elif current_command[0] == 'Rearrange':
        if current_command[1] in initial_groceries_list:
            initial_groceries_list.remove(current_command[1])
            initial_groceries_list.append(current_command[1])

    command = input()

print(', '.join(initial_groceries_list))