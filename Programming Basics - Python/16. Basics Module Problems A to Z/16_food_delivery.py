chicken_menus_count = int(input())
fish_menus_count = int(input())
veggie_menus_count = int(input())

chicken_menu_price = 10.35
fish_menu_price = 12.40
veggie_menu_price = 8.15
delivery_cost = 2.50

chicken_price = chicken_menus_count * chicken_menu_price
fish_price = fish_menus_count * fish_menu_price
veggie_price = veggie_menus_count * veggie_menu_price
dessert_price = (chicken_price + fish_price + veggie_price) * 0.20

total_price = chicken_price + fish_price + veggie_price + dessert_price + delivery_cost

print(total_price)


