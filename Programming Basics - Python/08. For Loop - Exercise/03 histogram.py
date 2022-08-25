n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(1, n + 1):
    current_num = int(input())

    if current_num < 200:
        p1 = p1 + 1
    elif current_num < 400:
        p2 = p2 + 1
    elif current_num < 600:
        p3 = p3 + 1
    elif current_num < 800:
        p4 = p4 + 1
    else:
        p5 = p5 + 1

p1_percentage = p1 / n * 100
p2_percentage = p2 / n * 100
p3_percentage = p3 / n * 100
p4_percentage = p4 / n * 100
p5_percentage = p5 / n * 100

print(f'{p1_percentage:.2f}%')
print(f'{p2_percentage:.2f}%')
print(f'{p3_percentage:.2f}%')
print(f'{p4_percentage:.2f}%')
print(f'{p5_percentage:.2f}%')