orders_dictionary = {}
command = input()

while command != 'buy':
    command = command.split()
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])
    if product in orders_dictionary:
        orders_dictionary[product] = [price, (quantity + orders_dictionary[product][1])]
    else:
        orders_dictionary[product] = [price, quantity]

    command = input()

for element in orders_dictionary:
    total_sum = orders_dictionary[element][0] * orders_dictionary[element][1]
    print(f'{element} -> {total_sum:.2f}')