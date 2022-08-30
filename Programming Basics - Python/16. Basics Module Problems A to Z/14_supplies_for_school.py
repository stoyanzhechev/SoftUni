pen_count = int(input())
marker_count = int(input())
detergent_count = int(input())
discount_percentage = int(input())

pen_price = 5.80
marker_price = 7.20
detergent_price = 1.20

total_cost = pen_count * pen_price + marker_count * marker_price + \
    detergent_count * detergent_price
total_cost -= total_cost * discount_percentage / 100

print(total_cost)