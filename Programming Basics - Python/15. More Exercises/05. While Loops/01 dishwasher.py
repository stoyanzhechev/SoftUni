detergent_bottles = int(input())

total_detergent_available = detergent_bottles * 750

dishes_count = 0
pots_count = 0
counter = 0

command = input()
while command != 'End':
    count = int(command)
    counter += 1
    if counter % 3 != 0:
        dishes_count += count
        total_detergent_available -= count * 5
    else:
        pots_count += count
        total_detergent_available -= count * 15

    if total_detergent_available < 0:
        print(f'Not enough detergent, {abs(total_detergent_available)} ml. more necessary!')
        break

    command = input()

if total_detergent_available >= 0:
    print('Detergent was enough!')
    print(f'{dishes_count} dishes and {pots_count} pots were washed.')
    print(f'Leftover detergent {total_detergent_available} ml.')

