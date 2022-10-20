def palindrome_string(word):
    if word == word[::-1]:
        return word


initial_list = input().split()
palindrome = input()
palindrome_list = [word for word in initial_list if palindrome_string(word)]
palindromes_count = palindrome_list.count(palindrome)
print(palindrome_list)
print(f'Found palindrome {palindromes_count} times')
