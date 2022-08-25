movie_type = input()
rows = int(input())
columns = int(input())

total_seats = rows * columns

price = 0

if movie_type == 'Premiere':
    price = 12.00
elif movie_type == 'Normal':
    price = 7.50
elif movie_type == 'Discount':
    price = 5.00

total_income = total_seats * price

print(f'{total_income:.2f} leva')