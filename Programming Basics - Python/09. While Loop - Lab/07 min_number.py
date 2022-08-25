input_num = input()
min_num = 10000000000000

while input_num != "Stop":
    num = int(input_num)

    if num < min_num:
        min_num = num

    input_num = input()

print(min_num)