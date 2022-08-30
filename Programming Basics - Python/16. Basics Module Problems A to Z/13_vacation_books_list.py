pages_count = int(input())
pages_per_hour = int(input())
days_per_book = int(input())

time_for_a_book = pages_count / pages_per_hour
time_required_per_day = int(time_for_a_book / days_per_book)

print(time_required_per_day)