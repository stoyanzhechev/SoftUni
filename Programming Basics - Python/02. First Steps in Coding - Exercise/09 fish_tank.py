length = int(input())
width = int(input())
height = int(input())
fill_percentage = float(input())

total_volume_cm3 = length * width * height
total_volume_ltrs = total_volume_cm3 / 1000
fill_percentage_ltrs = (total_volume_ltrs * fill_percentage) / 100

free_volume = total_volume_ltrs - fill_percentage_ltrs

print(free_volume)