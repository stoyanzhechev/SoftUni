# •	Пакет химикали - 5.80 лв.
# •	Пакет маркери - 7.20 лв.
# •	Препарат - 1.20 лв (за литър)

pens = int(input())
markers = int(input())
detergent = int(input())
discount_percentage = int(input())

pens_cost = pens * 5.80
markers_cost = markers * 7.20
detergent_cost = detergent * 1.20

total_cost = pens_cost + markers_cost + detergent_cost
discount = (total_cost * discount_percentage) / 100

grand_total = total_cost - discount

print(grand_total)