targets_sequence = list(map(int, input().split()))
command = input()
shot_targets_counter = 0

while command != 'End':
    index = int(command)
    if 0 <= index < len(targets_sequence) and targets_sequence[index] != -1:
        shot_targets_counter += 1
        current_value = targets_sequence[index]
        for target_index in range(len(targets_sequence)):
            if targets_sequence[target_index] == -1:
                continue
            if targets_sequence[target_index] > current_value:
                targets_sequence[target_index] -= current_value
            else:
                targets_sequence[target_index] += current_value
        targets_sequence[index] = -1
    command = input()

target_sequence_converted_to_string = [str(num) for num in targets_sequence]
print(f"Shot targets: {shot_targets_counter} -> {' '.join(target_sequence_converted_to_string)}")