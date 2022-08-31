budget = float(input())
gpu_count = int(input())
cpu_count = int(input())
ram_count = int(input())

gpu_cost = gpu_count * 250
cpu_cost = gpu_cost * 0.35 * cpu_count
ram_cost = gpu_cost * 0.10 * ram_count

total_cost = gpu_cost + cpu_cost + ram_cost

if gpu_count > cpu_count:
    total_cost *= 0.85

diff = abs(budget - total_cost)

if budget >= total_cost:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")