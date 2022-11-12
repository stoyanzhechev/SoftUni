items = {"shards": 0, "fragments": 0, "motes": 0}
current_items = input().split()
legendary_item_obtained = False

while not legendary_item_obtained:
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index + 1].lower()
        if key not in items.keys():
            items[key] = 0
        items[key] += value
        if items["shards"] >= 250:
            print("Shadowmourne obtained!")
            items["shards"] -= 250
            legendary_item_obtained = True
        elif items["fragments"] >= 250:
            print("Valanyr obtained!")
            items["fragments"] -= 250
            legendary_item_obtained = True
        elif items["motes"] >= 250:
            print("Dragonwrath obtained!")
            items["motes"] -= 250
            legendary_item_obtained = True
        if legendary_item_obtained:
            break
    if legendary_item_obtained:
        break
    current_items = input().split()

for material, quantity in items.items():
    print(f"{material}: {quantity}")