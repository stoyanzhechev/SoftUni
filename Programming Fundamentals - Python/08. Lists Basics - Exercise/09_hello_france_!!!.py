collection_list = input(). split('|')
budget = float(input())
bought_items_price_list = []
profit = 0

for element in collection_list:
    bought_item = element.split('->')
    item_type = bought_item[0]
    item_value = float(bought_item[1])
    if budget < item_value:
        break
    if item_type == 'Clothes' and item_value <= 50.00:
        budget -= item_value
        sold_price = item_value * 1.40
        profit += sold_price - item_value
    elif item_type == 'Shoes' and item_value <= 35.00:
        budget -= item_value
        sold_price = item_value * 1.40
        profit += sold_price - item_value
    elif item_type == 'Accessories' and item_value <= 20.50:
        budget -= item_value
        sold_price = item_value * 1.40
        profit += sold_price - item_value
    else:
        continue
    bought_items_price_list.append(round(sold_price, 2))


final_bought_list = ' '.join(map(str, bought_items_price_list))
print(final_bought_list)
print(f'Profit: {profit:.2f}')

new_budget = budget + sum(bought_items_price_list)

if new_budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')



