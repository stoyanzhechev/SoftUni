messages_count = int(input())

for i in range(messages_count):
    current_message = int(input())
    if current_message == 88:
        print('Hello')
    elif current_message == 86:
        print('How are you?')
    elif current_message != 86 and current_message < 88:
        print('GREAT!')
    elif current_message > 88:
        print('Bye.')