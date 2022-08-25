available_food_kg = int(input())

input_line = ''
counter = 0
eaten_food = 0
available_food_gr = available_food_kg * 1000

while True:
    input_line = input()
    if input_line == 'Adopted':
        break
    else:
        input_line = int(input_line)
        eaten_food += input_line
        counter += 1

    diff = abs(eaten_food - available_food_gr)

if eaten_food <= available_food_gr:
    print(f'Food is enough! Leftovers: {diff} grams.')
else:
    print(f'Food is not enough. You need {diff} grams more.')