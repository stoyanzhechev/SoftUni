breadth = int(input())
length = int(input())
total_pieces = breadth * length
pieces_left = True

command = input()
while command != 'STOP':
    pieces_taken = int(command)
    total_pieces -= pieces_taken
    if total_pieces < 0:
        diff = abs(total_pieces)
        pieces_left = False
        break
    command = input()

if not pieces_left:
    print(f"No more cake left! You need {diff} pieces more.")
else:
    print(f"{total_pieces} pieces are left." )


