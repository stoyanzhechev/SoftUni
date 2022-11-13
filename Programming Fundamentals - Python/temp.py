resources = {}
command = input()

while command != 'stop':
    current_resource = command
    current_quantity = int(input())
    if current_resource not in resources.keys():
        resources[current_resource] = 0
    resources[current_resource] += current_quantity
    command = input()

for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")