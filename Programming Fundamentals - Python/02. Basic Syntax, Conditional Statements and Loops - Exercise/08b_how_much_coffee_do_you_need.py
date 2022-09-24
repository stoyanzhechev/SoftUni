total_coffee = 0

while True:
    command = input()
    if command != 'END':
        if command == 'coding' or command == 'dog' or command == 'cat' or command == 'movie':
            total_coffee += 1
        elif command == 'CODING' or command == 'DOG' or command == 'CAT' or command == 'MOVIE':
            total_coffee += 2
    else:
        break

if total_coffee > 5:
    print('You need extra sleep')
else:
    print(total_coffee)

