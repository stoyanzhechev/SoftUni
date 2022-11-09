phonebook = {}

while True:
    entry = input()
    if '-' not in entry:
        break
    name, phone = entry.split('-')
    phonebook[name] = phone
for check in range(int(entry)):
    searched_name = input()
    if searched_name in phonebook.keys():
        found_number = phonebook[searched_name]
        print(f'{searched_name} -> {found_number}')
    else:
        print(f'Contact {searched_name} does not exist.')
