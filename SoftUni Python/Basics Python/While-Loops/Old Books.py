book_name = input()
book_count = 0
Is_book_found = False
current_book = input()

while current_book != "No More Books":
    if current_book == book_name:
        Is_book_found = True
        print(f'You checked {book_count} books and found it.')
        break

    book_count += 1
    current_book = input()

if not Is_book_found:
    print(f'The book you search is not here!')
    print(f'You checked {book_count} books.')
