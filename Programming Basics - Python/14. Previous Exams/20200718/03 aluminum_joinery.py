parts_count = int(input())
part_type = input()
delivery = input()

part_price = 0
part_discount = 0
total_price = 0

if parts_count < 10:
    print('Invalid order')
else:
    if part_type == '90X130':
        part_price = 110
        total_price = part_price * parts_count
        if 30 < parts_count <= 60:
            discount = 5
            total_price *= 0.95
        elif parts_count > 60:
            discount = 8
            total_price *= 0.92
    elif part_type == '100X150':
        part_price = 140
        total_price = part_price * parts_count
        if 40 < parts_count <= 80:
            discount = 6
            total_price *= 0.94
        elif parts_count > 80:
            discount = 10
            total_price *= 0.90
    elif part_type == '130X180':
        part_price = 190
        total_price = part_price * parts_count
        if 20 < parts_count <= 50:
            discount = 7
            total_price *= 0.93
        elif parts_count > 50:
            discount = 12
            total_price *= 0.88
    elif part_type == '200X300':
        part_price = 250
        total_price = part_price * parts_count
        if 25 < parts_count <= 50:
            discount = 9
            total_price *= 0.91
        elif parts_count > 50:
            discount = 14
            total_price *= 0.86

    if delivery == 'With delivery':
        total_price += 60
    elif delivery == 'Without delivery':
        total_price += 0

    if parts_count > 99:
        total_price *= 0.96

    print(f"{total_price:.2f} BGN")

