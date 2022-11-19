courses = {}
command = input()

while command != 'end':
    command = command.split(' : ')
    course = command[0]
    student = command[1]
    if course not in courses.keys():
        courses[course] = []
    courses[course].append(student)

    command = input()

for course in courses.keys():
    print(f'{course}: {len(courses[course])}')
    for student in courses[course]:
        print(f'-- {student}')

