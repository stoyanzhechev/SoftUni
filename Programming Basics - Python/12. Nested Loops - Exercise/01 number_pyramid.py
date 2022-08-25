num = int(input())
counter = 1
num_is_reached = False

for row in range(1, num + 1):
    for column in range(1, row + 1):
        print(counter, end=' ')
        counter += 1
        if counter > num:
            num_is_reached = True
            break
    if num_is_reached:
        break
    print()