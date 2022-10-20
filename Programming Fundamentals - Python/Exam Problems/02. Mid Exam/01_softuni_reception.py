first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
number_of_students = int(input())
hours_counter = 0

overall_efficiency = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency

while number_of_students > 0:
    number_of_students -= overall_efficiency
    hours_counter += 1
    if hours_counter % 4 == 0:
        hours_counter += 1
print(f"Time needed: {hours_counter}h.")

