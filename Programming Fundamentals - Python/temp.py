commands_number = int(input())
users = {}

for command in range(commands_number):
    current_command = input().split()
    command_action = current_command[0]
    if command_action == 'register':
        command_username = current_command[1]
        command_license_plate = current_command[2]
        if command_username in users.keys():
            print(f"ERROR: already registered with plate number {command_license_plate}")
        else:
            users[command_username] = command_license_plate
            print(f"{command_username} registered {command_license_plate} successfully")
    elif command_action == 'unregister':
        command_username = current_command[1]
        if command_username not in users.keys():
            print(f"ERROR: user {command_username} not found")
        else:
            del users[command_username]
            print(f"{command_username} unregistered successfully")

for username, license_plate_number in users.items():
    print(f"{username} => {license_plate_number}")
