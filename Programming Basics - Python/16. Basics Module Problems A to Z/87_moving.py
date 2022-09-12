breadth = int(input())
length = int(input())
height = int(input())
available_space = breadth * length * height
there_is_enough_space = True

command = input()
while command != 'Done':
    boxes = int(command)
    available_space -= boxes
    if available_space < 0:
        there_is_enough_space = False
        diff = abs(available_space)
        break
    command = input()
if there_is_enough_space:
    print(f"{available_space} Cubic meters left.")
else:
    print(f"No more free space! You need {diff} Cubic meters more.")