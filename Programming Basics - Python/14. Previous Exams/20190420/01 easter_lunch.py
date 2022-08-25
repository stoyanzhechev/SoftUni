cakes_count = int(input())
eggs_group_count = int(input())
cookies_count = int(input())

eggs_count = eggs_group_count * 12

cakes_cost = cakes_count * 3.20
eggs_cost = eggs_group_count * 4.35
cookies_cost = cookies_count * 5.40
egg_paint_cost = eggs_count * 0.15

total_cost = cakes_cost + eggs_cost + cookies_cost + egg_paint_cost

print(f'{total_cost:.2f}')
