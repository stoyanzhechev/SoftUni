book_pages = int(input())
pages_per_hour = int(input())
allowed_days = int(input())

time_per_book = book_pages // pages_per_hour
hours_per_day = time_per_book // allowed_days

print(hours_per_day)