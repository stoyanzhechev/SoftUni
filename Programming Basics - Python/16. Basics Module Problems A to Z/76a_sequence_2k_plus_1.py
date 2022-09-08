input_number = int(input())

current_num = 1

while True:
    print(current_num)
    current_num = current_num * 2 + 1
    if current_num > input_number:
        break