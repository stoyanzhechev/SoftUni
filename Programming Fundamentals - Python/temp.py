divisor = int(input())
boundary = int(input())

for n in range(1, boundary - 1):
    if n % divisor == 0:
        print(n)
        break