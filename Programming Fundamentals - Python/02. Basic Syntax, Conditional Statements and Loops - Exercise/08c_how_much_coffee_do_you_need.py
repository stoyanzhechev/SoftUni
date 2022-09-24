total_coffee = 0

command = input()
while command != 'END':
    if command.lower() == 'coding' \
        or command.lower() == 'dog' \
        or command.lower() == 'cat' \
        or command.lower() == 'movie':
        if command.islower():
            total_coffee += 1
        else: # if command.isupper()
            total_coffee += 2

    command = input()

if total_coffee > 5:
    print("You need extra sleep")
else:
    print(total_coffee)

