jury_count = int(input())

presentations_count = 0
final_assessment = 0

command = input()

while command != 'Finish':
    current_presentation_name = command
    presentations_count += 1
    current_presentation_grade = 0
    for presentation_grade in range(jury_count):
        current_grade = float(input())
        current_presentation_grade += current_grade
    current_presentation_average = current_presentation_grade / jury_count
    print(f'{current_presentation_name} - {current_presentation_average:.2f}.')
    final_assessment += current_presentation_average
    command = input()

final_average_grade = final_assessment / presentations_count

print(f"Student's final assessment is {final_average_grade:.2f}.")