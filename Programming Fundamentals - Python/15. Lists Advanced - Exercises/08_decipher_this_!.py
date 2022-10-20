secret_message = input().split()
deciphered_message = []

for message in secret_message:
    number = ''
    current_message = ''
    for character in message:
        if character.isdigit():
            number += character
        else:
            break
    message = message.replace(number, '')
    number = int(number)
    current_message += chr(number)
    if len(message) >= 2:
        message = message[-1] + message[1:-1] + message[0]
    current_message += message
    deciphered_message.append(current_message)
print(' '.join(deciphered_message))
