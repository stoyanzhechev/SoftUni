number = int(input())

for i in range(0, number + 1):
    if i % 2 == 0:
        result = 2 ** i
        print(result)