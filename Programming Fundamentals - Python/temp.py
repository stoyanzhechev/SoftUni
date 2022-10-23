command = input()
chat_list = []

while command != 'end':
    command = command.split()
    command_action = command[0]
    command_message = command[1]
    if command_action == 'Chat':
        chat_list.append(command_message)
    elif command_action == 'Delete':
        if command_message in chat_list:
            chat_list.remove(command_message)
    elif command_action == 'Edit':
        edited_message = command[2]
        if command_message in chat_list:
            for element in range(len(chat_list)):
                if chat_list[element] == command_message:
                    chat_list[element] = edited_message
    elif command_action == 'Pin':
        if command_message in chat_list:
            command_message_index = chat_list.index(command_message)
            removed_item = chat_list[command_message_index]
            chat_list.remove(removed_item)
            chat_list.append(removed_item)
    if command_action == 'Spam':
        message_index = 0
        for index in range(len(command)):
            current_message = command[message_index + index]
            chat_list.append(current_message)
            if 'Spam' in chat_list:
                chat_list.remove('Spam')

    command = input()

print('\n'.join(chat_list))