# •	Пилешко меню –  10.35 лв.
# •	Меню с риба – 12.40 лв.
# •	Вегетарианско меню  – 8.15 лв.

chicken = int(input())
fish = int(input())
veggie = int(input())

chicken_cost = chicken * 10.35
fish_cost = fish * 12.40
veggie_cost = veggie * 8.15
dessert_cost = (chicken_cost + fish_cost + veggie_cost) * 0.20
delivery_cost = 2.50

total_cost = chicken_cost + fish_cost + veggie_cost + dessert_cost + delivery_cost

print(total_cost)
