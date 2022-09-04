tabs_count = int(input())
salary = int(input())

for i in range(tabs_count):
    open_website = input()
    if open_website == 'Facebook':
        salary -= 150
    elif open_website == 'Instagram':
        salary -= 100
    elif open_website == 'Reddit':
        salary -= 50
    else:
        salary -= 0

if salary <= 0:
    print("You have lost your salary.")
else:
    print(f'{salary:.0f}')