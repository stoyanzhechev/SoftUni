contest_stage = input()
ticket_type = input()
ticket_count = int(input())
trophy_photo = input()

ticket_price = 0

if contest_stage == 'Quarter final':
    if ticket_type == 'Standard':
        ticket_price = 55.50
    elif ticket_type == 'Premium':
        ticket_price = 105.20
    elif ticket_type == 'VIP':
        ticket_price = 118.90
elif contest_stage == 'Semi final':
    if ticket_type == 'Standard':
        ticket_price = 75.88
    elif ticket_type == 'Premium':
        ticket_price = 125.22
    elif ticket_type == 'VIP':
        ticket_price = 300.40
elif contest_stage == 'Final':
    if ticket_type == 'Standard':
        ticket_price = 110.10
    elif ticket_type == 'Premium':
        ticket_price = 160.66
    elif ticket_type == 'VIP':
        ticket_price = 400.00

total_price = ticket_price * ticket_count

if total_price > 4000:
    grand_total_price = total_price * 0.75
elif total_price > 2500:
    grand_total_price = total_price * 0.90

if trophy_photo == 'Y' and total_price > 4000:
    print(f'{grand_total_price:.2f}')
elif trophy_photo == 'Y' and total_price > 2500:
    print(f'{(grand_total_price + ticket_count * 40):.2f}')
elif trophy_photo == 'N' and total_price > 2500:
    print(f'{grand_total_price:.2f}')
elif trophy_photo == 'Y' and total_price <= 2500:
    print(f'{(total_price+ ticket_count * 40):.2f}')
elif trophy_photo == 'N' and total_price <= 2500:
    print(f'{total_price:.2f}')