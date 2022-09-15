sold_games = int(input())
hearthstone_sold_count = 0
fornite_sold_count = 0
overwatch_sold_count = 0
others_sold_count = 0

for i in range(sold_games):
    current_game = input()
    if current_game == 'Hearthstone':
        hearthstone_sold_count += 1
    elif current_game == 'Fornite':
        fornite_sold_count += 1
    elif current_game == 'Overwatch':
        overwatch_sold_count += 1
    else:
        others_sold_count += 1

hearthstone_percentage = hearthstone_sold_count / sold_games * 100
fornite_percentage = fornite_sold_count / sold_games * 100
overwatch_percentage = overwatch_sold_count / sold_games * 100
others_percentage = others_sold_count / sold_games * 100

print(f"Hearthstone - {hearthstone_percentage:.2f}%")
print(f"Fornite - {fornite_percentage:.2f}%")
print(f"Overwatch - {overwatch_percentage:.2f}%")
print(f"Others - {others_percentage:.2f}%")