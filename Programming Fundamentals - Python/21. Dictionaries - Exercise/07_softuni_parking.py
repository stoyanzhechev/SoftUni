cars_number = int(input())
parking = {}
for car in range(cars_number):
    current_driver = input().split()
    action = current_driver[0]
    if action == 'register':
        username = current_driver[1]
        license_plate_number = current_driver[2]
        if username in parking.keys():
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            parking[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    elif action == 'unregister':
        username = current_driver[1]
        if username not in parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            del parking[username]
            print(f"{username} unregistered successfully")

for username, license_plate_number in parking.items():
    print(f"{username} => {license_plate_number}")