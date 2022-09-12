current_sum = float(input())
current_sum = int(current_sum * 100)
coins_counter = 0

if current_sum >= 200:
    coins_counter += current_sum // 200
    current_sum -= coins_counter * 200
if current_sum >= 100:
    coins_counter += current_sum // 100
    current_sum -= coins_counter * 100
if current_sum >= 50:
    coins_counter += current_sum // 50
    current_sum -= coins_counter * 50
if current_sum >= 20:
    coins_counter += current_sum // 20
    current_sum -= coins_counter * 20
if current_sum >= 10:
    coins_counter += current_sum // 10
    current_sum -= coins_counter * 10
if current_sum >= 5:
    coins_counter += current_sum // 5
    current_sum -= coins_counter * 10
if current_sum >= 2:
    coins_counter += current_sum // 2
    current_sum -= coins_counter * 2
if current_sum >= 1:
    coins_counter += current_sum

print(coins_counter)
