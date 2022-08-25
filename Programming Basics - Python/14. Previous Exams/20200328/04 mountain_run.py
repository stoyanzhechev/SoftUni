import math

record_sec = float(input())
distance_mtr = float(input())
time_per_mtr = float(input())

time = distance_mtr * time_per_mtr
delays_count = math.floor(distance_mtr / 50)
delay = delays_count * 30

total_time = time + delay

diff = abs(total_time - record_sec)

if total_time < record_sec:
    print(f'Yes! The new record is {total_time:.2f} seconds.')
else:
    print(f'No! He was {diff:.2f} seconds slower.')
