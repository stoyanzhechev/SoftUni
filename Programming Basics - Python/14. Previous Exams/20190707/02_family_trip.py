budget = float(input())
nights_count = int(input())
price_per_night = float(input())
misc_costs_percentage = int(input())

if nights_count > 7:
    price_per_night *= 0.95
total_nights_price = nights_count * price_per_night
total_misc_costs = budget * (misc_costs_percentage / 100)
total_costs = total_misc_costs + total_nights_price
diff = abs(budget - total_costs)
if budget >= total_costs:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")