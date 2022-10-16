number_of_rooms = int(input())
free_chairs = 0
needed_chairs = 0
sum_of_needed_chairs = 0

for room in range(1, number_of_rooms + 1):
    current_room = input().split()
    current_room_chairs = len(current_room[0])
    current_room_visitors = int(current_room[1])
    if current_room_chairs > current_room_visitors:
        free_chairs += current_room_chairs - current_room_visitors
    elif current_room_chairs < current_room_visitors:
        needed_chairs = abs(current_room_chairs - current_room_visitors)
        sum_of_needed_chairs += needed_chairs
        print(f"{needed_chairs} more chairs needed in room {room}")

if free_chairs >= sum_of_needed_chairs:
    print(f"Game On, {free_chairs} free chairs left")

