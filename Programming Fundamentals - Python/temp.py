architect_name = input()
projects_count = int(input())
time_per_project = 3

time_required = projects_count * time_per_project

print(f'The architect {architect_name} will need {time_required} hours to complete {projects_count} project/s.')