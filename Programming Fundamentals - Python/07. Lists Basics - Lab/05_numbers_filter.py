n = int(input())
even_list = []
odd_list = []
negative_list = []
positive_list = []

for i in range(n):
    current_num = int(input())

    if current_num % 2 == 0:
        even_list.append(current_num)
    if current_num >= 0:
        positive_list.append(current_num)
    if current_num % 2 == 1:
        odd_list.append(current_num)
    if current_num < 0:
        negative_list.append(current_num)

command = input()

if command == 'even':
    print(even_list)
elif command == 'odd':
    print(odd_list)
elif command == 'positive':
    print(positive_list)
elif command == 'negative':
    print(negative_list)