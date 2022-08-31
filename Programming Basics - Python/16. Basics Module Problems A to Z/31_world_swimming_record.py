world_record_secs = float(input())
distance_meters = float(input())
time_per_1_meter = float(input())

initial_time = distance_meters * time_per_1_meter
delays_count = distance_meters // 15
total_delays = delays_count * 12.5
total_time = initial_time + total_delays
diff = abs(world_record_secs - total_time)

if total_time < world_record_secs:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
