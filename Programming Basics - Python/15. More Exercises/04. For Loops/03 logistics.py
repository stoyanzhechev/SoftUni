cargo_count = int(input())

total_weight = 0

car_weight = 0
truck_weight = 0
train_weight = 0

car_cost = 0
truck_cost = 0
train_cost = 0

for current_cargo in range(cargo_count):
    cargo_weight = int(input())
    total_weight += cargo_weight
    if cargo_weight <= 3:
        car_cost += cargo_weight * 200
        car_weight += cargo_weight
    elif cargo_weight <= 11:
        truck_cost += cargo_weight * 175
        truck_weight += cargo_weight
    else:
        train_cost += cargo_weight * 120
        train_weight += cargo_weight

average_cost = (car_cost + truck_cost + train_cost) / total_weight

car_percentage = car_weight / total_weight * 100
truck_percentage = truck_weight / total_weight * 100
train_percentage = train_weight / total_weight * 100

print(f'{average_cost:.2f}')
print(f'{car_percentage:.2f}%')
print(f'{truck_percentage:.2f}%')
print(f'{train_percentage:.2f}%')


