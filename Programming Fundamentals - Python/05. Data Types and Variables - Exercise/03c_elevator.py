number_of_people = int(input())
elevator_capacity = int(input())
number_of_courses = 0

while number_of_people >= 0:
    if number_of_people > elevator_capacity:
        number_of_people -= elevator_capacity
        number_of_courses += 1
    else:
        number_of_courses += 1
        break
print(number_of_courses)
