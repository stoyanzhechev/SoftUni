students_count = int(input())

first_grade_studs_count = 0
second_grade_studs_count = 0
third_grade_studs_count = 0
forth_grade_studs_count = 0

total_score = 0

for students in range(students_count):
    grade = float(input())
    total_score += grade
    if grade >= 5:
        first_grade_studs_count += 1
    elif grade >= 4:
        second_grade_studs_count += 1
    elif grade >= 3:
        third_grade_studs_count += 1
    else:
        forth_grade_studs_count += 1

first_grade_percentage = first_grade_studs_count / students_count * 100
second_grade_percentage = second_grade_studs_count / students_count * 100
third_grade_percentage = third_grade_studs_count / students_count * 100
forth_grade_percentage = forth_grade_studs_count / students_count * 100
average_grade = total_score / students_count

print(f"Top students: {first_grade_percentage:.2f}%")
print(f"Between 4.00 and 4.99: {second_grade_percentage:.2f}%")
print(f"Between 3.00 and 3.99: {third_grade_percentage:.2f}%")
print(f"Fail: {forth_grade_percentage:.2f}%")
print(f'Average: {average_grade:.2f}')
