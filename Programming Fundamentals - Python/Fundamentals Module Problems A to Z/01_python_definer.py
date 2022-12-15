input_number = float(input())

if input_number == 0:
    print('zero')
elif input_number > 0:
    if 0 < input_number < 1:
        print('small positive')
    elif 1 <= input_number <= 1000000:
        print('positive')
    else:
        print('large positive')
else:
    if -1 < input_number < 0:
        print('small negative')
    elif -1000000 <= input_number <= -1:
        print('negative')
    else:
        print('large negative')