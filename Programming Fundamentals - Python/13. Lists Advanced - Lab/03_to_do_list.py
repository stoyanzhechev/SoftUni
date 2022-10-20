to_do_list = []

while True:
    command = input()
    if command == 'End':
        break

    current_note = command.split('-')
    importance_index = int(current_note[0])
    command_action = current_note[1]

    to_do_list.append([importance_index, command_action])

sorted_to_do_list = [current_note[1] for current_note in sorted(to_do_list)]

print(sorted_to_do_list)
