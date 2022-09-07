max_poor_grades = int(input())
total_score = 0
problems_count = 0
poor_grades_count = 0
command = input()

while command != 'Enough':
    problem_name = command
    problem_grade = int(input())
    problems_count += 1
    total_score += problem_grade
    if problem_grade <= 4:
        poor_grades_count += 1
        if poor_grades_count == max_poor_grades:
            print(f"You need a break, {poor_grades_count} poor grades.")
            break

    command = input()

if poor_grades_count < max_poor_grades:
    average_grade = total_score / problems_count
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {problems_count}")
    print(f"Last problem: {problem_name}")