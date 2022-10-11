input_string = input()
number_of_repetitions = int(input())

output_string = lambda a, b: a * b
result = output_string(input_string, number_of_repetitions)

print(result)
