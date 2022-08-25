first_player_egg_count = int(input())
second_player_egg_count = int(input())

command = input()
while command != 'End':
    if command == 'one':
        second_player_egg_count -= 1
    elif command == 'two':
        first_player_egg_count -= 1

    if first_player_egg_count == 0:
        print(f"Player one is out of eggs. Player two has {second_player_egg_count} eggs left.")
        break
    elif second_player_egg_count == 0:
        print(f"Player two is out of eggs. Player one has {first_player_egg_count} eggs left.")
        break
    command = input()

else:
    print(f"Player one has {first_player_egg_count} eggs left.")
    print(f"Player two has {second_player_egg_count} eggs left.")