n = int(input())

even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    num = int(input())
    if i % 2 == 0:
        even_sum = even_sum + num
    else:
        odd_sum = odd_sum + num

if even_sum == odd_sum:
    print('Yes')
    print(f'Sum = {odd_sum}')
else:
    diff = abs(odd_sum - even_sum)
    print('No')
    print(f'Diff = {diff}')


