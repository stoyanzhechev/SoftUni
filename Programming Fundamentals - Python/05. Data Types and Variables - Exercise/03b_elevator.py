number_of_people = int(input())
elevator_capacity = int(input())
number_of_courses = 0

if number_of_people % elevator_capacity == 0:
    number_of_courses = number_of_people // elevator_capacity
else:
    number_of_courses = number_of_people // elevator_capacity + 1

print(number_of_courses)