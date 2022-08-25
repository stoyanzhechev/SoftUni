days = int(input())
accommodation_type = input()
assessment = input()

nights = (days - 1)
single_room_price = 18.00
apartment_price = 25
president_apartment_price = 35
total_cost = 0
grand_total_cost = 0

if accommodation_type == 'room for one person':
    total_cost = single_room_price * nights
elif accommodation_type == 'apartment':
    total_cost = apartment_price * nights
    if nights < 9:
        total_cost = 0.70 * total_cost
    elif 9 <= nights <= 14:
        total_cost = 0.65 * total_cost
    else:
        total_cost = 0.50 * total_cost
elif accommodation_type == 'president apartment':
    total_cost = president_apartment_price * nights
    if nights < 9:
        total_cost = 0.90 * total_cost
    elif 9 <= nights <= 14:
        total_cost = 0.85 * total_cost
    else:
        total_cost = 0.80 * total_cost

if assessment == 'positive':
    grand_total_cost = total_cost * 1.25
elif assessment == 'negative':
    grand_total_cost = total_cost * 0.90

print(f'{grand_total_cost:.2f}')

