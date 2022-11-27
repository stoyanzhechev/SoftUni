concealed_message = input()
instructions_input = input()

while instructions_input != 'Reveal':
    command = instructions_input.split(':|:')
    if command[0] == 'InsertSpace':
        index = int(command[1])
        concealed_message = concealed_message[:index] + ' ' + concealed_message[index:]
        print(concealed_message)
    elif command[0] == 'Reverse':
        substring = command[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, '', 1)
            concealed_message = concealed_message + substring[::-1]
            print(concealed_message)
        else:
            print('error')
    elif command[0] == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)

    instructions_input = input()

print(f'You have a new text message: {concealed_message}')
