chicken_count = int(input())
fish_count = int(input())
veggie_count = int(input())

chicken_price = 10.35
fish_price = 12.40
veggie_price = 8.15

chicken_cost = chicken_count * chicken_price
fish_cost = fish_count * fish_price
veggie_cost = veggie_count * veggie_price
dessert_cost = (chicken_cost + fish_cost + veggie_cost) * 0.20
delivery_cost = 2.50

grand_total_cost = chicken_cost + fish_cost + veggie_cost + dessert_cost + delivery_cost

print(grand_total_cost)