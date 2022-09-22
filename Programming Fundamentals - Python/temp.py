number_of_orders = int(input())
grand_total_price = 0

for current_order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    total_order_price = price_per_capsule * capsules_per_day * days
    grand_total_price += total_order_price
    print(f"The price for the coffee is: ${total_order_price:.2f}")
print(f"Total: ${grand_total_price:.2f}")