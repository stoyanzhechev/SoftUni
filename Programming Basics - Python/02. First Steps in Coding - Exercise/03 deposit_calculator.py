deposit_sum = float(input())
deposit_duration = int(input())
annual_interest_percentage = float(input())

annual_interest = annual_interest_percentage / 100
sum = deposit_sum + deposit_duration * ((deposit_sum * annual_interest) / 12)

print(sum)

