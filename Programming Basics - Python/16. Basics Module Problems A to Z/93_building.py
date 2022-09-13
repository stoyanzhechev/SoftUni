floors = int(input())
rooms = int(input())

for f in range(floors, 0, -1):
    for r in range(rooms):
        print(f'{f}{r}', end=' ')
    print()