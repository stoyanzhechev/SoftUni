fruit = input()
set_type = input()
set_count = int(input())

set_items = 0
item_price = 0
set_price = 0

if set_type == 'small':
    set_items = 2
    if fruit == 'Watermelon':
        set_price = set_items * 56.00
    elif fruit == 'Mango':
        set_price = set_items * 36.66
    elif fruit == 'Pineapple':
        set_price = set_items * 42.10
    elif fruit == 'Raspberry':
        set_price = set_items * 20.00

elif set_type == 'big':
    set_items = 5
    if fruit == 'Watermelon':
        set_price = set_items * 28.70
    elif fruit == 'Mango':
        set_price = set_items * 19.60
    elif fruit == 'Pineapple':
        set_price = set_items * 24.80
    elif fruit == 'Raspberry':
        set_price = set_items * 15.20

total_price = set_price * set_count

if 400 <= total_price <= 1000:
    total_price = 0.85 * total_price
elif total_price > 1000:
    total_price = 0.50 * total_price

print(f'{total_price:.2f} lv.')