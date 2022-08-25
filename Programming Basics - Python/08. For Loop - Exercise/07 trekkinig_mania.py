groups_count = int(input())

musala_count = 0
monblan_count = 0
kilimandjaro_count = 0
k2_count = 0
everest_count = 0
total_count = 0

for i in range(1, groups_count + 1):
    people = int(input())
    total_count = total_count + people

    if people <= 5:
        musala_count = musala_count + people
    elif people <= 12:
        monblan_count = monblan_count + people
    elif people <= 25:
        kilimandjaro_count = kilimandjaro_count + people
    elif people <= 40:
        k2_count = k2_count + people
    else:
        everest_count = everest_count + people

print(f'{musala_count / total_count * 100:.2f}%')
print(f'{monblan_count / total_count * 100:.2f}%')
print(f'{kilimandjaro_count / total_count * 100:.2f}%')
print(f'{k2_count / total_count * 100:.2f}%')
print(f'{everest_count / total_count * 100:.2f}%')


