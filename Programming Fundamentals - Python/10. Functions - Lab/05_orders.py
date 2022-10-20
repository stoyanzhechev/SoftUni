def order_price(beverage, number):
    if order == 'coffee':
        return quantity * 1.50
    elif order == 'water':
        return quantity * 1.00
    elif order == 'coke':
        return quantity * 1.40
    elif order == 'snacks':
        return quantity * 2.00


order = input()
quantity = int(input())
print(f'{order_price(order, quantity):.2f}')