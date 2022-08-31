length_cm = int(input())
breadth_cm = int(input())
height_cm = int(input())
fill_percentage = float(input())

length_dm = length_cm / 10
breadth_dm = breadth_cm / 10
height_dm = height_cm / 10

total_volume = length_dm * breadth_dm * height_dm
total_available_volume = total_volume - fill_percentage * total_volume / 100

print(total_available_volume)
