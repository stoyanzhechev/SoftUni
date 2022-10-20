initial_schedule = input().split(', ')
command = input()
lesson_index = 0

while command != 'course start':
    current_command = input().split(':')
    current_action = current_command[0]
    current_lesson = current_command[1]
    if current_action == 'Add' and current_lesson not in initial_schedule:
        initial_schedule.append(current_lesson)
    elif current_action == 'Insert' and current_lesson not in initial_schedule:
        lesson_index = current_command[2]
        initial_schedule.insert(lesson_index, current_lesson)
    elif current_action == 'Remove' and current_lesson not in initial_schedule:
        initial_schedule.remove(current_lesson)
    elif current_action == 'Swap' and current_lesson in initial_schedule:
        new_lesson = current_command[2]
        current_lesson, new_lesson = new_lesson, current_lesson
    elif current_action == 'Exercise':
        pass
    lesson_index += 1
    command = input()
