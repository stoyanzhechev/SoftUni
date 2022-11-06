items = input().split()
bakery_dictionary = {}
for index in range(0, len(items), 2):
    key = items[index]
    value = int(items[index + 1])
    bakery_dictionary[key] = value
print(bakery_dictionary)
