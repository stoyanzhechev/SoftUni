pens_packets = int(input())
markers_packets = int(input())
detergent = int(input())
discount_percentage = int(input())

pens_price = 5.80
markers_price = 7.20
detergent_price = 1.20

pens_total_price = pens_packets * pens_price
markers_total_price = markers_packets * markers_price
detergent_total_price = detergent * detergent_price

total_price = pens_total_price + markers_total_price + detergent_total_price
discounted_price = total_price * (100 - discount_percentage) / 100

print(discounted_price)