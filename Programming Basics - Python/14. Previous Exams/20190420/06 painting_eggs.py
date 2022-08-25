egg_size = input()
egg_color = input()
egg_count = int(input())

price = 0

if egg_size == 'Large':
    if egg_color == 'Red':
        price = 16
    elif egg_color == 'Green':
        price = 12
    elif egg_color == 'Yellow':
        price = 9
elif egg_size == 'Medium':
    if egg_color == 'Red':
        price = 13
    elif egg_color == 'Green':
        price = 9
    elif egg_color == 'Yellow':
        price = 7
elif egg_size == 'Small':
    if egg_color == 'Red':
        price = 9
    elif egg_color == 'Green':
        price = 8
    elif egg_color == 'Yellow':
        price = 5

total_egg_price = price * egg_count
manufacturing_cost = total_egg_price * 0.35

grand_total_cost = total_egg_price - manufacturing_cost

print(f"{grand_total_cost:.2f} leva.")

