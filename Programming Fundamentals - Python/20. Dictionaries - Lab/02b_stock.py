items = input().split()
bakery = {}
searched_products = input().split()

for index in range(0, len(items), 2):
    key = items[index]
    value = items[index + 1]
    bakery[key] = value

for product in searched_products:
    if product in bakery.keys():
        quantity = bakery[product]
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
