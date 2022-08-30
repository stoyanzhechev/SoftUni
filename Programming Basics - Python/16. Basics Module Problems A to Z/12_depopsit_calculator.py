initial_deposit = float(input())
deposit_duration = int(input())
annual_interest_rate = float(input())

accrued_interest = (initial_deposit * annual_interest_rate / 100) * deposit_duration / 12
total_amount = initial_deposit + accrued_interest

print(total_amount)