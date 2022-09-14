town = input()
package = input()
vip_discount = input()
stay_days = int(input())
is_valid = True

price = 0

if town == 'Bansko' or town == 'Borovets':
    if package == 'withEquipment':
        price = 100
        if vip_discount == 'yes':
            price *= 0.90
    elif package == 'noEquipment':
        price = 80
        if vip_discount == 'yes':
            price *= 0.95
elif town == 'Varna' or town == 'Burgas':
    if package == 'withBreakfast':
        price = 130
        if vip_discount == 'yes':
            price *= 0.88
    elif package == 'noBreakfast':
        price = 100
        if vip_discount == 'yes':
            price *= 0.93
else:
    is_valid = False

total_cost = stay_days * price

if not is_valid:
    print("Invalid input!")
else:
    if stay_days > 1:
        print(f"The price is {total_cost:.2f}lv! Have a nice time!")
    elif stay_days < 1:
        print("Days must be positive number!")





