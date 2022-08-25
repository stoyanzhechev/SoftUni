minutes_per_walk = int(input())
walks_counts_daily = int(input())
cal_per_day = int(input())

cal_burnt_per_walk = minutes_per_walk * 5
cal_burnt_per_day = cal_burnt_per_walk * walks_counts_daily

if cal_burnt_per_day >= (cal_per_day * 0.50):
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {cal_burnt_per_day}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {cal_burnt_per_day}.')
