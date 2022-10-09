groceries_list = input().split('!')
command = input()

while command != 'Go Shopping!':
    current_command = command.split()
    command_info = current_command[0]
    if command_info == 'Urgent':
        item = current_command[1]
        if item not in groceries_list:
            groceries_list.insert(0, item)
    elif command_info == 'Unnecessary':
        item = current_command[1]
        if item in groceries_list:
            groceries_list.remove(item)
    elif command_info == 'Correct':
        old_item = current_command[1]
        new_item = current_command[2]
        if old_item in groceries_list:
            index = groceries_list.index(old_item)
            groceries_list[index] = new_item
    elif command_info == 'Rearrange':
        item = current_command[1]
        if item in groceries_list:
            groceries_list.remove(item)
            groceries_list.append(item)

    command = input()

print(', '.join(groceries_list))
