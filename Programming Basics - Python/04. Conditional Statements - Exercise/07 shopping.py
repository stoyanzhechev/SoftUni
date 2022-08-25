budget = float(input())
vga_count = int(input())
cpu_count = int(input())
ram_count = int(input())

vga_price = 250
cpu_price = (vga_count * vga_price) * 0.35
ram_price = (vga_count * vga_price) * 0.10

total_cost = vga_count * vga_price + cpu_count * cpu_price + ram_count * ram_price

if vga_count > cpu_count:
    total_cost = total_cost * 0.85

diff = abs(total_cost - budget)

if total_cost <= budget:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')