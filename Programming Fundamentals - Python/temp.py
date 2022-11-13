items_dictionary = {'shards': 0, 'fragments': 0, 'motes': 0}
current_items = input().split()
legendary_is_obtained = False

while not legendary_is_obtained:
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index + 1].lower()
        if key not in items_dictionary.keys():
            items_dictionary[key] = 0
        items_dictionary[key] += value
        if items_dictionary['shards'] >= 250:
            legendary_is_obtained = True
            items_dictionary['shards'] -= 250
            print('Shadowmourne obtained!')
        elif items_dictionary['fragments'] >= 250:
            legendary_is_obtained = True
            items_dictionary['fragments'] -= 250
            print('Valanyr obtained!')
        elif items_dictionary['motes'] >= 250:
            legendary_is_obtained = True
            items_dictionary['motes'] -= 250
            print('Dragonwrath obtained!')
        if legendary_is_obtained:
            break
    if legendary_is_obtained:
        break

    current_items = input().split()

for material, quantity in items_dictionary.items():
    print(f"{material}: {quantity}")



