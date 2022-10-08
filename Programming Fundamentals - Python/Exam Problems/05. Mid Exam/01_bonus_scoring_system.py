from math import ceil

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
attended_lectures = 0

for current_student in range(number_of_students):
    student_attendances = int(input())
    total_bonus = student_attendances / number_of_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        attended_lectures = student_attendances

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {attended_lectures} lectures.")




