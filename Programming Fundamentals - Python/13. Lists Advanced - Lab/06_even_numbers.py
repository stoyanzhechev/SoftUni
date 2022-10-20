integers_list = list(map(int, input().split(', ')))
even_numbers_indices = [num for num in range(len(integers_list)) if integers_list[num] % 2 == 0]
print(even_numbers_indices)
