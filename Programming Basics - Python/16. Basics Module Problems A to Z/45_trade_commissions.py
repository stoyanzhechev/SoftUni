town = input()
sales = float(input())

commission = 0

if town == 'Sofia' and sales >= 0:
    if 0 <= sales <= 500:
        commission = 5.0
    elif 500 < sales <= 1000:
        commission = 7.0
    elif 1000 < sales <= 10000:
        commission = 8.0
    else:
        commission = 12.0
elif town == 'Varna' and sales >= 0:
    if 0 <= sales <= 500:
        commission = 4.5
    elif 500 < sales <= 1000:
        commission = 7.5
    elif 1000 < sales <= 10000:
        commission = 10.0
    else:
        commission = 13.0
elif town == 'Plovdiv' and sales >= 0:
    if 0 <= sales <= 500:
        commission = 5.5
    elif 500 < sales <= 1000:
        commission = 8.0
    elif 1000 < sales <= 10000:
        commission = 12.0
    else:
        commission = 14.5
else:
    print('error')

total_commission = sales * commission / 100

if total_commission > 0:
    print(f'{total_commission:.2f}')