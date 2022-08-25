btc_count = int(input())
cny_count = float(input())
comm = float(input())

usd_count = 0

btc_bgn = btc_count * 1168
cny_usd = cny_count * 0.15
usd_bgn = cny_usd * 1.76

available_bgn = btc_bgn + usd_bgn

available_eur = available_bgn / 1.95

total_eur = available_eur * (100 - comm) / 100

print(f'{total_eur:.2f}')