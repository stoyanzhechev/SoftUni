guest_count = int(input())
individual_price = float(input())
budget = float(input())

cake_price = budget * 0.10

if 10 <= guest_count <= 15:
    individual_price *= 0.85
elif 15 < guest_count <= 20:
    individual_price *= 0.80
elif guest_count > 20:
    individual_price *= 0.75

total_price = individual_price * guest_count
grand_total_price = cake_price + total_price
diff = abs(budget - grand_total_price)

if budget >= grand_total_price:
    print(f"It is party time! {diff:.2f} leva left.")
else:
    print(f"No party! {diff:.2f} leva needed.")