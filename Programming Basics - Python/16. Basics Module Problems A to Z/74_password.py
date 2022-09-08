user_name = input()
user_password = input()

input_password = input()
while input_password != user_password:
    input_password = input()

print(f'Welcome {user_name}!')