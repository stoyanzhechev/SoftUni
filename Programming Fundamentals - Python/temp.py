phonebook = {}

while True:
    current_input = input()
    if '-' not in current_input:
        break
    name, phone = current_input.split('-')
    phonebook[name] = phone
for check in range(int(current_input)):
    searched_name = input()
    if searched_name in phonebook.keys():
        found_number = phonebook[searched_name]
        print(f"{searched_name} -> {found_number}")
    else:
        print(f"Contact {searched_name} does not exist.")

