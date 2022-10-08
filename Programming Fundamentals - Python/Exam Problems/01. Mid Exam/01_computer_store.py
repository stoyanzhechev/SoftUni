command = input()
total_price = 0
special_discount = False
invalid_order = False

while command != 'special' and command != 'regular':
    part_price = float(command)
    if part_price < 0:
        part_price = 0
        print('Invalid price!')
    total_price += part_price
    command = input()
else:
    if command == 'special':
        special_discount = True

if total_price == 0:
    invalid_order = True

if invalid_order:
    print('Invalid order!')
else:
    total_tax = total_price * 0.2
    grand_total_price = total_price + total_tax

    if special_discount:
        grand_total_price *= 0.90

    print(f"""Congratulations you've just bought a new computer! 
Price without taxes: {total_price:.2f}$ 
Taxes: {total_tax:.2f}$
-----------
Total price: {grand_total_price:.2f}$""")

