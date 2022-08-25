tabs_count = int(input())
salary = int(input())

current_salary = salary

for i in range(1, tabs_count + 1):
    web_site = input()
    if web_site == 'Facebook':
        current_salary = current_salary - 150
    elif web_site == 'Instagram':
        current_salary = current_salary - 100
    elif web_site == 'Reddit':
        current_salary = current_salary - 50
    else:
        current_salary = current_salary

if current_salary <= 0:
    print('You have lost your salary.')
else:
    print(f'{current_salary}')