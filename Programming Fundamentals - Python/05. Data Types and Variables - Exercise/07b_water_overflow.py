number_of_pours = int(input())
filled_capacity = 0

for i in range(number_of_pours):
    current_pour = int(input())
    if (255 - filled_capacity) < current_pour:
        print('Insufficient capacity!')
    else:
        filled_capacity += current_pour
print(filled_capacity)
