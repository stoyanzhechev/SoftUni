groups_count = int(input())

total_count = 0
musala_count = 0
monblan_count = 0
kili_count = 0
k2_count = 0
everest_count = 0
people = 0

for i in range(1, groups_count + 1):
    people = int(input())
    total_count += people

    if people <= 5:
        musala_count += people
    elif people <= 12:
        monblan_count += people
    elif people <= 25:
        kili_count += people
    elif people <= 40:
        k2_count += people
    else:
        everest_count += people

musala_percentage = musala_count / total_count * 100
monblan_percentage = monblan_count / total_count * 100
kili_percentage = kili_count / total_count * 100
k2_percentage = k2_count / total_count * 100
everest_percentage = everest_count / total_count * 100

print(f'{musala_percentage:.2f}%')
print(f'{monblan_percentage:.2f}%')
print(f'{kili_percentage:.2f}%')
print(f'{k2_percentage:.2f}%')
print(f'{everest_percentage:.2f}%')