greening_area = float(input())
price_per_sqm = 7.61

total_price = greening_area * price_per_sqm
discount = 0.18 * total_price
discounted_price = 0.82 * total_price

print(f"The final price is: {discounted_price:.2f} lv.")
print(f"The discount is: {discount} lv.")

