name = input()
grades_total = 0
year_counter = 0
fail_counter = 0

while True:
    annual_grade = float(input())
    year_counter += 1

    if annual_grade < 4:
        fail_counter += 1
        if fail_counter == 2:
            print(f'{name} has been excluded at {year_counter} grade')
            break

        year_counter -= 1

    else:
        grades_total += annual_grade

    if year_counter == 12:
        average_grade = grades_total / 12
        print(f'{name} graduated. Average grade: {average_grade:.2f}')
        break