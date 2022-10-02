number_of_lines = int(input())
key_word = input()
initial_list = []
key_word_list = []

for sentences in range(number_of_lines):
    current_sentence = input()
    initial_list.append(current_sentence)
    if key_word in current_sentence:
        key_word_list.append(current_sentence)

print(initial_list)
print(key_word_list)