month = input()
nights = int(input())

studio_price = 0
apartment_price = 0
studio_discount_percentage = 0
apartment_discount_percentage = 0

if month == 'May' or month == 'October':
    studio_price = 50.00
    apartment_price = 65.00
    if nights <= 7:
        studio_discount_percentage = 0
        apartment_discount_percentage = 0
    elif 7 < nights <= 14:
        studio_discount_percentage = 5
        apartment_discount_percentage = 0
    elif nights > 14:
        studio_discount_percentage = 30
        apartment_discount_percentage = 10
elif month == 'June' or month == 'September':
    studio_price = 75.20
    apartment_price = 68.70
    if nights <= 7:
        studio_discount_percentage = 0
        apartment_discount_percentage = 0
    elif 7 < nights <= 14:
        studio_discount_percentage = 0
        apartment_discount_percentage = 0
    elif nights > 14:
        studio_discount_percentage = 20
        apartment_discount_percentage = 10
elif month == 'July' or month == 'August':
    studio_price = 76.00
    apartment_price = 77.00
    if nights <= 7:
        studio_discount_percentage = 0
        apartment_discount_percentage = 0
    elif 7 < nights <= 14:
        studio_discount_percentage = 0
        apartment_discount_percentage = 0
    elif nights > 14:
        studio_discount_percentage = 0
        apartment_discount_percentage = 10

total_cost_studio = (nights * studio_price) * (100 - studio_discount_percentage) / 100
total_cost_apartment = (nights * apartment_price) * (100 - apartment_discount_percentage) / 100

print(f'Apartment: {total_cost_apartment:.2f} lv.')
print(f'Studio: {total_cost_studio:.2f} lv.')