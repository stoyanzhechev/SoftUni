people_count = int(input())
elevator_capacity = int(input())

courses = 0

for current_course in range(people_count):
    courses += 1
    people_count -= elevator_capacity
    if people_count > 0:
        continue
    else:
        break

print(courses)

# people_count = int(input())
# elevator_capacity = int(input())
#
# courses = 0
#
# if people_count % elevator_capacity == 0:
#     courses = int(people_count / elevator_capacity)
# else:
#     courses = int(people_count / elevator_capacity) + 1
#
# print(courses)