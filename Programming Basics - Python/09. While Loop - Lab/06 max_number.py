input_num = input()
max_num = -10000000000000

while input_num != "Stop":
    num = int(input_num)

    if num > max_num:
        max_num = num

    input_num = input()

print(max_num)




