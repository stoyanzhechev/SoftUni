company_name = input()
adult_tickets_count = int(input())
child_ticket_count = int(input())
net_adult_price = float(input())
misc_tax = float(input())

net_child_ticket = 0.3 * net_adult_price

total_adult_ticket_price = net_adult_price + misc_tax
total_child_ticket_price = net_child_ticket + misc_tax

total_tickets_sold_income = total_adult_ticket_price * adult_tickets_count + total_child_ticket_price * child_ticket_count

net_profit = 0.2 * total_tickets_sold_income

print(f"The profit of your agency from {company_name} tickets is {net_profit:.2f} lv.")