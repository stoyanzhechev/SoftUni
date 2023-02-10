deposit_amount = float(input())
deposit_duration = int(input())
annual_interest_rate = float(input())

final_amount = deposit_amount + deposit_duration * (deposit_amount * (annual_interest_rate / 100)) / 12

print(final_amount)


