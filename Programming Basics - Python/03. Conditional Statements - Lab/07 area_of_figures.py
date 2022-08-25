# Pay specific attention to the exponentiation formula (lines 10, 19)
# Pay specific attention to the rounding at the bottom of the code (line 26)

import math

shape = input()

if shape == 'square':
    side = float(input())
    shape_area = side ** 2

elif shape == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    shape_area = side_a * side_b

elif shape == 'circle':
    rad = float(input())
    shape_area = math.pi * (rad ** 2)

else:
    side_a = float(input())
    height_h = float(input())
    shape_area = (side_a * height_h) / 2

print(f'{shape_area:.3f}')
