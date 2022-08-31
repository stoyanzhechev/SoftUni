fruit = input()
week_day = input()
quantity = float(input())

product_price = 0

if week_day == 'Monday' or week_day == 'Tuesday' or week_day == 'Wednesday' or \
    week_day == 'Thursday' or week_day == 'Friday':
    if fruit == 'banana':
        product_price = 2.50
    elif fruit == 'apple':
        product_price = 1.20
    elif fruit == 'orange':
        product_price = 0.85
    elif fruit == 'grapefruit':
        product_price = 1.45
    elif fruit == 'kiwi':
        product_price = 2.70
    elif fruit == 'pineapple':
        product_price = 5.50
    elif fruit == 'grapes':
        product_price = 3.85
    else:
        print('error')
elif week_day == 'Saturday' or week_day == 'Sunday':
    if fruit == 'banana':
        product_price = 2.70
    elif fruit == 'apple':
        product_price = 1.25
    elif fruit == 'orange':
        product_price = 0.90
    elif fruit == 'grapefruit':
        product_price = 1.60
    elif fruit == 'kiwi':
        product_price = 3.00
    elif fruit == 'pineapple':
        product_price = 5.60
    elif fruit == 'grapes':
        product_price = 4.20
    else:
        print('error')
else:
    print('error')

total_price = quantity * product_price

if total_price > 0:
    print(f'{total_price:.2f}')
