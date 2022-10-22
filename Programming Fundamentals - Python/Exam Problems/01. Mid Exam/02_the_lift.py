waiting_people = int(input())
current_lift_state = list(map(int, input().split()))

for wagon in range(len(current_lift_state)):
    if waiting_people > 3:
        current_group = 4 - current_lift_state[wagon]
        waiting_people -= current_group
        current_lift_state[wagon] += current_group
    else:
        current_lift_state[wagon] += waiting_people
        waiting_people = 0

if waiting_people > 0:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
    print(' '.join([str(num) for num in current_lift_state]))
elif sum(current_lift_state) != len(current_lift_state) * 4:
    print("The lift has empty spots!")
    print(' '.join([str(num) for num in current_lift_state]))
