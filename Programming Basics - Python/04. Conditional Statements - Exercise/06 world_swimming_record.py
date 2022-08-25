# Pay specific attention to the rounding to the smaller number in lines 8 and 9 - both lines are interchangeable

world_record = float(input())
distance = float(input())
time_per_meter = float(input())

total_time = distance * time_per_meter
delays_count = distance // 15
# delays_count = math.floor(distance_mtr / 15)
delays_time = delays_count * 12.5

grand_total_time = total_time + delays_time

diff = abs(grand_total_time - world_record)

if grand_total_time < world_record:
    print(f'Yes, he succeeded! The new world record is {grand_total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {diff:.2f} seconds slower.')