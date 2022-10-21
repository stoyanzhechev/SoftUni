neighborhood = [int(num) for num in input().split('@')]
command = input()
position = 0

while not command == 'Love!':
    jump_length = command.split()[1]
    jump_length = int(jump_length)

    position = position + jump_length

    if position >= len(neighborhood):
        position = 0

    if neighborhood[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        neighborhood[position] -= 2
        if neighborhood[position] == 0:
            print(f"Place {position} has Valentine's day.")
    command = input()

print(f"Cupid's last position was {position}.")

counter = 0
for number in neighborhood:
    if not number == 0:
        counter += 1

if counter == 0:
    print('Mission was successful.')
else:
    print(f"Cupid has failed {counter} places.")