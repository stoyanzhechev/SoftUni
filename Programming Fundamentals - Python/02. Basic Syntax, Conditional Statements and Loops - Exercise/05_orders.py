orders_count = int(input())

total_cost = 0

for current_order in range(orders_count):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    current_order_price = price_per_capsule * capsules_per_day * days
    total_cost += current_order_price
    print(f"The price for the coffee is: ${current_order_price:.2f}")

print(f"Total: ${total_cost:.2f}")
