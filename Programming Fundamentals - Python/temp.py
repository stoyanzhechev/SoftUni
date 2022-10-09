initial_loot_list = input().split('|')
command = input()
final_loot_list = initial_loot_list

while command != 'Yohoho!':
    command_action = command.split()
    if command_action[0] == 'Loot':
        pass
    elif command_action[0] == 'Drop':
        if int(command_action[1]) in initial_loot_list:
            initial_loot_list.pop[int(command_action[1])]
            dropped_item = initial_loot_list.pop[int(command_action[1])]
            initial_loot_list.append(dropped_item)
    elif command_action[0] == 'Steal':
        pass

    command= input()
