waiting_people = int(input())
current_lift_state = list(map(int, input().split()))
current_index = 0

for index in current_lift_state:
    if waiting_people // 4 >= 1:
        current_number_of_people = abs(4 - current_lift_state[current_index])
        current_lift_state[current_index] += current_number_of_people
        waiting_people -= current_number_of_people
        current_index += 1
    else:
        current_number_of_people = waiting_people % 4
        current_lift_state[current_index] += current_number_of_people
        waiting_people = 0

if waiting_people > 0:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
    print(' '.join([str(num) for num in current_lift_state]))
else:
    print("The lift has empty spots!")
    print(' '.join([str(num) for num in current_lift_state]))