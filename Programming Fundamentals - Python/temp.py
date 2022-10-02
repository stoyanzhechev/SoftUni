numbers_count = int(input())
even_list = []
odd_list = []
positives_list = []
negatives_list = []

for i in range(numbers_count):
    current_number = int(input())
    if current_number % 2 == 0:
        even_list.append(current_number)
    else:
        odd_list.append(current_number)
    if current_number >= 0:
        positives_list.append(current_number)
    else:
        negatives_list.append(current_number)

command = input()

if command == 'even':
    print(even_list)
elif command == 'odd':
    print(odd_list)
elif command == 'positive':
    print(positives_list)
elif command == 'negative':
    print(negatives_list)