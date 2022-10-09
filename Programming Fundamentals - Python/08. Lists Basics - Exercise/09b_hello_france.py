collection_of_items = input().split('|')
budget = float(input())
profit = 0
sum_of_sold_items = 0
condition = False

for item in collection_of_items:
    item_info = item.split('->')
    item_type = item_info[0]
    item_value = float(item_info[1])
    condition = False

    if item_type == 'Clothes' and item_value <= 50.00:
        condition = True
    elif item_type == 'Shoes' and item_value <= 35.00:
        condition = True
    elif item_type == 'Accessories' and item_value <= 20.50:
        condition = True
    else:
        continue

    if condition:
        if budget >= item_value:
            budget -= item_value
            sold_item_price = item_value * 1.40
            sum_of_sold_items += sold_item_price
            profit += sold_item_price - item_value
            print(f'{sold_item_price:.2f}', end=' ')
print()
print(f'Profit: {profit:.2f}')

final_budget = budget + sum_of_sold_items

if final_budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')



