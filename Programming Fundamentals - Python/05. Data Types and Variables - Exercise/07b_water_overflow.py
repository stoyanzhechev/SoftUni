number_of_pours = int(input())
filled_capacity = 0
sufficient_capacity = True

for i in range(number_of_pours):
    current_pour = int(input())
    if (255 - filled_capacity) < current_pour:
        sufficient_capacity = False
        print('Insufficient capacity!')
    else:
        filled_capacity += current_pour
print(filled_capacity)
