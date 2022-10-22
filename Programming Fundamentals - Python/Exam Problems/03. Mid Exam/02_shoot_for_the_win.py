def reduce_values(targets_sequence, index):
    special_value = targets_sequence[index]
    targets_sequence[index] = -1

    for i in range(len(targets_sequence)):
        if targets_sequence[i] == -1:
            continue
        if special_value < targets_sequence[i]:
            targets_sequence[i] -= special_value
        else:
            targets_sequence[i] += special_value

    return targets_sequence


def shoot_for_the_win_func(targets_sequence):
    count_of_shot_targets = 0

    while True:
        command = input()

        if command == 'End':
            break

        index = int(command)

        if 0 <= index < len(targets_sequence) and targets_sequence[index] != -1:
            count_of_shot_targets += 1
            reduce_values(targets_sequence, index)

    target_values_converted_to_string = [str(num) for num in targets_sequence]
    print(f"Shot targets: {count_of_shot_targets} -> {' '.join(target_values_converted_to_string)}")


data = list(map(int, input().split()))
shoot_for_the_win_func(data)
