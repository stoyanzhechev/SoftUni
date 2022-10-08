total_energy = 100
total_coins = 100
events_list = input().split('|')
bakery_is_open = True

for event in events_list:
    event_info = event.split('-')
    event_type = event_info[0]
    event_value = event_info[1]
    current_energy = total_energy
    if event_type == 'rest':
        temporary_energy = total_energy
        total_energy += int(event_value)
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - temporary_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif event_type == 'order':
        if current_energy >= 30:
            print(f'You earned {int(event_value)} coins.')
            total_coins += int(event_value)
            total_energy -= 30
        else:
            print(f'You had to rest!')
            total_energy += 50
    else:
        if total_coins >= int(event_value):
            total_coins -= int(event_value)
            print(f'You bought {event_type}.')
        else:
            bakery_is_open = False
            print(f'Closed! Cannot afford {event_type}.')
            break
if bakery_is_open:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")



