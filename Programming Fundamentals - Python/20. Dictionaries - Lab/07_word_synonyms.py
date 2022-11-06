number = int(input())
synonyms_dictionary = {}

for item in range(number):
    word = input()
    synonym = input()
    if word not in synonyms_dictionary:
        synonyms_dictionary[word] = []
    synonyms_dictionary[word].append(synonym)

for word in synonyms_dictionary:
    print(f"{word} - {', '.join(synonyms_dictionary[word])}")
