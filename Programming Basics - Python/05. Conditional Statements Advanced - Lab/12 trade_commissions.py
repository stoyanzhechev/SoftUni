town = input()
sales = float(input())

commission = 0

if town == 'Sofia':
    if 0 <= sales <= 500:
        commission = 5
    elif 500 < sales <= 1000:
        commission = 7
    elif 1000 < sales <= 10000:
        commission = 8
    elif sales > 10000:
        commission = 12
    else:
        commission = 0
elif town == 'Varna':
    if 0 <= sales <= 500:
        commission = 4.5
    elif 500 < sales <= 1000:
        commission = 7.5
    elif 1000 < sales <= 10000:
        commission = 10
    elif sales > 10000:
        commission = 13
    else:
        commission = 0
elif town == 'Plovdiv':
    if 0 <=  sales <= 500:
        commission = 5.5
    elif 500 < sales <= 1000:
        commission = 8
    elif 1000 < sales <= 10000:
        commission = 12
    elif sales > 10000:
        commission = 14.5
    else:
        commission = 0

total_commission = sales * commission / 100

if total_commission == 0:
    print('error')
else:
    print(f'{total_commission:.2f}')