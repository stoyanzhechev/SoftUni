student_name = input()
total_score = 0
grades_counter = 1
failed_attempts = 0

while grades_counter <= 12:
    if failed_attempts > 1:
        break
    current_grade = float(input())

    if current_grade < 4:
        failed_attempts += 1
        continue

    total_score += current_grade

    grades_counter += 1

if failed_attempts > 1:
    print(f"{student_name} has been excluded at {grades_counter} grade")
else:
    average_score = total_score / 12
    print(f"{student_name} graduated. Average grade: {average_score:.2f}")
