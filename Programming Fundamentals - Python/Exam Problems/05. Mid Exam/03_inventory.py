journal = input().split(', ')
command = input()

while command != 'Craft!':
    current_command = command.split(' - ')
    command_info = current_command[0]
    item = current_command[1]
    if command_info == 'Collect':
        if item not in journal:
            journal.append(item)
    elif command_info == 'Drop':
        if item in journal:
            journal.remove(item)
    elif command_info == 'Combine Items':
        item = item.split(':')
        old_item = item[0]
        new_item = item[1]
        if old_item in journal:
            index = int(journal.index(old_item))
            journal.insert(index + 1, new_item)
    elif command_info == 'Renew':
        if item in journal:
            journal.remove(item)
            journal.append(item)

    command = input()

print(', '.join(journal))