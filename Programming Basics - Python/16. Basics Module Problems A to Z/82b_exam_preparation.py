max_failed_attempts = int(input())
total_score = 0
failed_attempts = 0
problems_count = 0
has_failed = False

while True:
    command = input()
    if command != 'Enough':
        problem_name = command
    else:
        break
    problem_score = int(input())
    if problem_score <= 4:
        failed_attempts += 1
    if failed_attempts == max_failed_attempts:
        has_failed = True
        break
    total_score += problem_score
    problems_count += 1

if has_failed:
    print(f"You need a break, {failed_attempts} poor grades.")
else:
    average_score = total_score / problems_count
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {problems_count}")
    print(f"Last problem: {problem_name}")