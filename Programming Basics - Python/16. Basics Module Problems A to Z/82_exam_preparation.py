max_failed_attempts = int(input())
total_score = 0
problems_count = 0
failed_problems_count = 0
has_failed = False

command = input()
while command != 'Enough':
    problem_name = command
    problem_score = int(input())
    if problem_score <= 4:
        failed_problems_count += 1
        if failed_problems_count == max_failed_attempts:
            has_failed = True
            break
    total_score += problem_score
    problems_count += 1
    command = input()

if has_failed:
    print(f"You need a break, {failed_problems_count} poor grades.")
else:
    average_score = total_score / problems_count
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {problems_count}")
    print(f"Last problem: {problem_name}")