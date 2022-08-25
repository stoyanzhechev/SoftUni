sum_needed = int(input())

total_cash_payment = 0
total_card_payment = 0
total_money_raised = 0
cash_payments_count = 0
card_payments_count = 0
counter = 0

command = input()
while command != 'End':
    amount_per_payment = int(command)
    counter += 1
    if counter % 2 != 0:
        if amount_per_payment <= 100:
            total_cash_payment += amount_per_payment
            cash_payments_count += 1
            print(f'Product sold!')
        else:
            print('Error in transaction!')
    else:
        if amount_per_payment >= 10:
            total_card_payment += amount_per_payment
            card_payments_count += 1
            print('Product sold!')
        else:
            print('Error in transaction!')

    total_money_raised = total_card_payment + total_cash_payment

    if total_money_raised >= sum_needed:
        average_cash_payment = total_cash_payment / cash_payments_count
        average_card_payment = total_card_payment / card_payments_count
        print(f"Average CS: {average_cash_payment:.2f}")
        print(f"Average CC: {average_card_payment:.2f}")
        break

    command = input()

else:
    print("Failed to collect required money for charity.")
