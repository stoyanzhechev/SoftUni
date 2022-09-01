stay_days = int(input())
room_type = input()
final_assessment = input()

stay_nights = stay_days - 1
room_price = 0
discount = 0
extra_discount = 0

if room_type == 'room for one person':
    room_price = 18.00
    discount = 0
elif room_type == 'apartment':
    room_price = 25.00
    if stay_days < 10:
        discount = 30
    elif 10 <= stay_days <= 15:
        discount = 35
    elif stay_days > 15:
        discount = 50
elif room_type == 'president apartment':
    room_price = 35.00
    if stay_days < 10:
        discount = 10
    elif 10 <= stay_days <= 15:
        discount = 15
    elif stay_days > 15:
        discount = 20

total_cost = stay_nights * room_price
discounted_total_cost = total_cost * ((100 - discount) / 100)

if final_assessment == 'positive':
    extra_discount = -25
elif final_assessment == 'negative':
    extra_discount = 10

grand_total_cost = discounted_total_cost * ((100 - extra_discount) / 100)

print(f'{grand_total_cost:.2f}')