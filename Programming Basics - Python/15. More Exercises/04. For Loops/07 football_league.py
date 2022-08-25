field_capacity = int(input())
fan_count = int(input())

a_count = 0
b_count = 0
v_count = 0
g_count = 0

for i in range(fan_count):
    current_fan = input()
    if current_fan == 'A':
        a_count += 1
    elif current_fan == 'B':
        b_count += 1
    elif current_fan == 'V':
        v_count += 1
    elif current_fan == 'G':
        g_count += 1

filled_percentage = fan_count / field_capacity * 100

a_percentage = a_count / fan_count * 100
b_percentage = b_count / fan_count * 100
v_percentage = v_count / fan_count * 100
g_percentage = g_count / fan_count * 100

print(f'{a_percentage:.2f}%')
print(f'{b_percentage:.2f}%')
print(f'{v_percentage:.2f}%')
print(f'{g_percentage:.2f}%')
print(f'{filled_percentage:.2f}%')

