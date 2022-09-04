age = int(input())
wash_machine_price = float(input())
toy_price = int(input())

total_money_even_bdays = 0
brother_money_count = 0
toys_count = 0

for current_year in range(1, age + 1):
    if current_year % 2 != 0:
        toys_count += 1
    else:
        brother_money_count += 1
        total_money_even_bdays += current_year * 10 / 2

total_money = total_money_even_bdays + toys_count * toy_price - brother_money_count

diff = abs(total_money - wash_machine_price)

if total_money >= wash_machine_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')