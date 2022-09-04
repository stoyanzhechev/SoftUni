username = input()
password = input()

command = input()

while command != password:
    command = input()
else:
    print(f'Welcome {username}!')