students_count = int(input())
grades = {}

for _ in range(students_count):
    name = input()
    grade = float(input())
    if name not in grades.keys():
        grades[name] = []
    grades[name].append(grade)

filtered_grades = {}
for student_name, grade in grades.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.50:
        filtered_grades[student_name] = average_grade

for student_name, grade in filtered_grades.items():
    print(f'{student_name} -> {grade:.2f}')