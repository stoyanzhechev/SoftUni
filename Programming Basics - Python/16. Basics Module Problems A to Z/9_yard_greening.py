total_area = float(input())

price_per_sqm = 7.61

total_greening_cost = total_area * price_per_sqm
discount = total_greening_cost * 0.18
total_discounted_cost = total_greening_cost * 0.82

print(f"The final price is: {total_discounted_cost:.2f} lv.")
print(f"The discount is: {discount} lv.")

