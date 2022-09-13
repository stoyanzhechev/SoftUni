from math import ceil

people_count = int(input())
entry_fee = float(input())
lounger_price = float(input())
umbrella_price = float(input())

total_ticket_price = people_count * entry_fee
total_lounger_price = ceil(people_count * 0.75) * lounger_price
total_umbrella_price = ceil(people_count / 2) * umbrella_price

total_price = total_ticket_price + total_lounger_price + total_umbrella_price

print(f"{total_price:.2f} lv.")