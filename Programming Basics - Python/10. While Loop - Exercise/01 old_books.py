book_name = input()

current_book = input()
counter = 0
is_book_found = False

while current_book != 'No More Books':
    if current_book == book_name:
        is_book_found = True
        break

    counter += 1
    current_book = input()

if is_book_found:
    print(f'You checked {counter} books and found it.')

else:
    print('The book you search is not here!')
    print(f'You checked {counter} books.')


