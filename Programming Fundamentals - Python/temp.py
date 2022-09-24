command = input()
total_coffee = 0
extra_sleep_needed = False

while command != 'END':
    if command == 'coding' or command == 'dog' or command == 'cat' or command == 'movie':
        total_coffee += 1
    elif command == 'CODING' or command == 'DOG' or command == 'CAT' or command == 'MOVIE':
        total_coffee += 2

    if total_coffee > 5:
        extra_sleep_needed = True
        break

    command = input()

if extra_sleep_needed:
    print("You need extra sleep")
else:
    print(total_coffee)