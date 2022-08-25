sum_prime_nums = 0
sum_nonprime_nums = 0
command = input()

while command != 'stop':
    current_num = int(command)
    if current_num < 0:
        print('Number is negative.')
    else:
        current_num_is_prime = True
        for number in range(2, current_num):
            if current_num % number == 0:
                current_num_is_prime = False
                break
        if current_num_is_prime:
            sum_prime_nums += current_num
        else:
            sum_nonprime_nums += current_num
    command = input()

print(f'Sum of all prime numbers is: {sum_prime_nums}')
print(f'Sum of all non prime numbers is: {sum_nonprime_nums}')