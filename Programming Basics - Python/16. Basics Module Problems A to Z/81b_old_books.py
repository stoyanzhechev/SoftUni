favorite_book = input()
books_counter = 0
book_found = False

while True:
    command = input()
    if command == favorite_book:
        book_found = True
        break

    if command == 'No More Books':
        print(f"The book you search is not here!\nYou checked {books_counter} books.")
        break
    books_counter += 1

if book_found:
    print(f"You checked {books_counter} books and found it.")