groups_count = int(input())

musala_people_count = 0
monblan_people_count = 0
kilimandjaro_people_count = 0
k2_people_count = 0
everest_people_count = 0
total_people = 0

for current_group in range(groups_count):
    group_count = int(input())
    total_people += group_count
    if group_count <= 5:
        musala_people_count += group_count
    elif group_count <= 12:
        monblan_people_count += group_count
    elif group_count <= 25:
        kilimandjaro_people_count += group_count
    elif group_count <= 40:
        k2_people_count += group_count
    else:
        everest_people_count += group_count

musala_percentage = musala_people_count / total_people * 100
monblan_percentage = monblan_people_count / total_people * 100
kilimandjaro_percentage = kilimandjaro_people_count / total_people * 100
k2_percentage = k2_people_count / total_people * 100
everest_percentage = everest_people_count / total_people * 100

print(f'{musala_percentage:.2f}%')
print(f'{monblan_percentage:.2f}%')
print(f'{kilimandjaro_percentage:.2f}%')
print(f'{k2_percentage:.2f}%')
print(f'{everest_percentage:.2f}%')

