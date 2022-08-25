total_kids_tickets = 0
total_student_tickets = 0
total_standard_tickets = 0

movie_name = input()

while movie_name != 'Finish':
    free_seats = int(input())
    sold_seats = 0
    for free_tickets in range(free_seats):
        current_ticket = input()
        if current_ticket == 'End':
            break
        elif current_ticket == 'student':
            total_student_tickets += 1
        elif current_ticket == 'kid':
            total_kids_tickets += 1
        elif current_ticket == 'standard':
            total_standard_tickets += 1
        sold_seats += 1
    percent_full_hall = sold_seats / free_seats * 100
    print(f"{movie_name} - {percent_full_hall:.2f}% full.")
    movie_name = input()

total_tickets = total_kids_tickets + total_student_tickets + total_standard_tickets
students_percentage = total_student_tickets / total_tickets * 100
kids_percentage = total_kids_tickets / total_tickets * 100
standard_percentage = total_standard_tickets / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{students_percentage:.2f}% student tickets.")
print(f"{standard_percentage:.2f}% standard tickets.")
print(f"{kids_percentage:.2f}% kids tickets.")