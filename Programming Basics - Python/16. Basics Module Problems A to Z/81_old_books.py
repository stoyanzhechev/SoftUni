favorite_book = input()
books_counter = 0
current_book = input()
is_book_found = False

while current_book != 'No More Books':
    books_counter += 1
    if current_book != favorite_book:
        current_book = input()
    else:
        books_counter -= 1
        is_book_found = True
        break

if is_book_found:
    print(f"You checked {books_counter} books and found it.")
else:
    print(f"The book you search is not here! \nYou checked {books_counter} books.")





