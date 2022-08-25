months_count = int(input())

water_per_month = 20
water_total = water_per_month * months_count
internet_per_month = 15
internet_total = internet_per_month * months_count
electricity_total = 0
other_total = 0

for months in range(months_count):
    electricity_per_month = float(input())
    electricity_total += electricity_per_month
    other_total += (electricity_per_month + internet_per_month + water_per_month) * 1.20

average = (water_total + electricity_total + internet_total + other_total) / months_count

print(f'Electricity: {electricity_total:.2f} lv')
print(f'Water: {water_total:.2f} lv')
print(f'Internet: {internet_total:.2f} lv')
print(f'Other: {other_total:.2f} lv')
print(f'Average: {average:.2f} lv')



