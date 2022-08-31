movie_budget = float(input())
cast_count = int(input())
apparel_price = float(input())

decor_price = movie_budget * 0.10
apparel_total_price = cast_count * apparel_price

if cast_count > 150:
    apparel_total_price *= 0.90

total_cost = decor_price + apparel_total_price
diff = abs(movie_budget - total_cost)

if movie_budget >= total_cost:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")

