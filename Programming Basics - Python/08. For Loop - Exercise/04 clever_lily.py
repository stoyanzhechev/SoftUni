age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toys_count = 0
money_count = 0
money = 10
brother_count = 0

for i in range(1, age + 1):
    if i % 2 != 0:
        toys_count = toys_count + 1
    else:
        money_count = money_count + money
        money = money + 10
        brother_count = brother_count + 1

result = (money_count + toys_count * toy_price) - brother_count

diff = abs(result - washing_machine_price)

if result >= washing_machine_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
