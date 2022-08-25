divisor = int(input())
boundary = int(input())

for current_num in range(boundary, divisor, -1):
    if current_num % divisor == 0 and current_num <= boundary:
        print(current_num)
        break
