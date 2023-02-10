pages_count = int(input())
pages_per_hour = int(input())
total_days_needed = int(input())

total_hours_needed = pages_count / pages_per_hour
hours_per_day = total_hours_needed // total_days_needed

print(int(hours_per_day))
