change_bgn = float(input())

change_coins = round(change_bgn * 100)

rest_change = 0
coins_count = 0

while change_coins > 0:
    if change_coins >= 200:
        coins_count += 1
        change_coins -= 200
    elif change_coins >= 100:
        coins_count += 1
        change_coins -= 100
    elif change_coins >= 50:
        coins_count += 1
        change_coins -= 50
    elif change_coins >= 20:
        coins_count += 1
        change_coins -= 20
    elif change_coins >= 10:
        coins_count += 1
        change_coins -= 10
    elif change_coins >= 5:
        coins_count += 1
        change_coins -= 5
    elif change_coins >= 2:
        coins_count += 1
        change_coins -= 2
    elif change_coins >= 1:
        coins_count += 1
        change_coins -= 1

print(coins_count)



