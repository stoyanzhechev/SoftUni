town = input()
package = input()
vip_discount = input()
stay_days = int(input())
invalid_input = False

price = 0
discount = 0

if town == 'Bansko' or town == 'Borovets':
    if package == 'withEquipment':
        price = 100
        if vip_discount == 'yes':
            discount = 10
        else:
            discount = 0
    elif package == 'noEquipment':
        price = 80
        if vip_discount == 'yes':
            discount = 5
        else:
            discount = 0
    else:
        invalid_input = True
elif town == 'Varna' or town == 'Burgas':
    if package == 'withBreakfast':
        price = 130
        if vip_discount == 'yes':
            discount = 12
        else:
            discount = 0
    elif package == 'noBreakfast':
        price = 100
        if vip_discount == 'yes':
            discount = 7
        else:
            discount = 0
    else:
        invalid_input = True
else:
    invalid_input = True

total_price_per_day = price * (100 - discount) / 100
total_price = total_price_per_day * stay_days

if stay_days > 7:
    total_price -= total_price_per_day

if stay_days >= 1 and not invalid_input:
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
elif stay_days < 1 and not invalid_input:
    print("Days must be positive number!")
else:
    print("Invalid input!")



