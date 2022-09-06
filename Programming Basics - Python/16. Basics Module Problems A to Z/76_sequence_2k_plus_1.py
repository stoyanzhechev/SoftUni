input_number = int(input())
new_number = 0

while True:
    new_number = new_number * 2 + 1

    if new_number > input_number:
        break

    print(new_number)

