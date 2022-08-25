trip_price = float(input())
puzzle_count = int(input())
doll_count = int(input())
teddy_count = int(input())
minion_count = int(input())
truck_count = int(input())

# •	Пъзел - 2.60 лв.
# •	Говореща кукла - 3 лв.
# •	Плюшено мече - 4.10 лв.
# •	Миньон - 8.20 лв.
# •	Камионче - 2 лв.

puzzle_price = puzzle_count * 2.60
doll_price = doll_count * 3.00
teddy_price = teddy_count * 4.10
minion_price = minion_count * 8.20
truck_price = truck_count * 2.00

total_toys_count = puzzle_count + doll_count + teddy_count + minion_count + truck_count
gross_income = puzzle_price + doll_price + teddy_price + minion_price + truck_price

if total_toys_count >= 50:
    gross_income = gross_income * 0.75

rent_cost = gross_income * 0.10

net_income = gross_income - rent_cost

diff = abs(net_income - trip_price)

if net_income >= trip_price:
    print(f'Yes! {diff:.2f} lv left.')
else:
    print(f'Not enough money! {diff:.2f} lv needed.')