vacation_cost = float(input())
puzzles_count = int(input())
dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

toys_count = puzzles_count + dolls_count + teddy_bears_count + minions_count + trucks_count
puzzles_total_price = puzzles_count * 2.60
dolls_total_price = dolls_count * 3.00
teddy_bears_total_price = teddy_bears_count * 4.10
minions_total_price = minions_count * 8.20
trucks_total_price = trucks_count * 2.00
total_toys_price = puzzles_total_price + dolls_total_price + teddy_bears_total_price + \
    minions_total_price + trucks_total_price

if toys_count >= 50:
    total_toys_price *= 0.75

shop_rent = total_toys_price * 0.10
net_income = total_toys_price - shop_rent
diff = abs(vacation_cost - net_income)

if net_income >= vacation_cost:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")

