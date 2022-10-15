input_string = input().split()
initial_palindrome = input()
palindrome_list = []

for phrase in input_string:
    if phrase == phrase[::-1]:
        palindrome_list.append(phrase)

print(palindrome_list)
initial_palindrome_found = palindrome_list.count(initial_palindrome)
print(f'Found palindrome {initial_palindrome_found} times')