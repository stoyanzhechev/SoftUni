month = input()
nights_count = int(input())

studio_price = 0
apartment_price = 0
studio_discount = 0
apartment_discount = 0

if month == 'May' or month == 'October':
    studio_price = 50.00
    apartment_price = 65.00
    if 7 < nights_count <= 14:
        studio_discount = 5
    elif nights_count > 14:
        studio_discount = 30
        apartment_discount = 10
elif month == 'June' or month == 'September':
    studio_price = 75.20
    apartment_price = 68.70
    if nights_count > 14:
        studio_discount = 20
        apartment_discount = 10
elif month == 'July' or month == 'August':
    studio_price = 76.00
    apartment_price = 77.00
    if nights_count > 14:
        apartment_discount = 10

total_studio_price = (nights_count * studio_price) * ((100 - studio_discount) / 100)
total_apartment_price = (nights_count * apartment_price) * ((100 - apartment_discount) / 100)

print(f"Apartment: {total_apartment_price:.2f} lv.")
print(f"Studio: {total_studio_price:.2f} lv.")
