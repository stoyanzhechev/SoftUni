greening_area = float(input())

price_sqm = 7.61
discount_percentage = 18

final_price = (greening_area * price_sqm) * 0.82
discount = (greening_area * price_sqm) * 0.18

print(f'The final price is: {final_price} lv.')
print(f'The discount is: {discount} lv.')
