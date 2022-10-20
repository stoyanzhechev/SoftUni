total_health = 100
total_bitcoin = 0
dungeons_counter = 0
dungeons_list = input().split('|')
still_alive = True

for current_dungeon in dungeons_list:
    dungeon_info = current_dungeon.split()
    dungeon_command = dungeon_info[0]
    dungeon_value = int(dungeon_info[1])
    if dungeon_command == 'potion':
        dungeons_counter += 1
        healed_amount = abs(100 - total_health)
        total_health += dungeon_value
        if total_health > 100:
            total_health = 100
            print(f"You healed for {healed_amount} hp.")
        else:
            print(f"You healed for {dungeon_value} hp.")
        print(f"Current health: {total_health} hp.")
    elif dungeon_command == 'chest':
        dungeons_counter += 1
        total_bitcoin += dungeon_value
        print(f"You found {dungeon_value} bitcoins.")
    else:
        total_health -= dungeon_value
        dungeons_counter += 1
        if total_health > 0:
            print(f"You slayed {dungeon_command}.")
        else:
            print(f"You died! Killed by {dungeon_command}.")
            print(f'Best room: {dungeons_counter}')
            still_alive = False
            break

if still_alive:
    print("You've made it!")
    print(f"Bitcoins: {total_bitcoin}")
    print(f"Health: {total_health}")
