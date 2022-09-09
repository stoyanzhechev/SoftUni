favorite_book = input()
books_counter = 0
book_found = False

command = input()
while command != 'No More Books':
    if command == favorite_book:
        book_found = True
        break
    books_counter += 1

    command = input()

if book_found:
    print(f"You checked {books_counter} books and found it.")
else:
    print(f"The book you search is not here!\nYou checked {books_counter} books.")
