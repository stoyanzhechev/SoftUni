from math import pi

figure_type = input()

figure_area = 0

if figure_type == 'square':
    a = float(input())
    figure_area = a ** 2
elif figure_type == 'rectangle':
    a = float(input())
    b = float(input())
    figure_area = a * b
elif figure_type == 'circle':
    r = float(input())
    figure_area = pi * r ** 2
elif figure_type == 'triangle':
    a = float(input())
    h = float(input())
    figure_area = a * h / 2

print(f'{figure_area:.3f}')