class Book:
    def __init__(self, title, author, publication_year, available=True):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.available = available
    
    def borrow_book(self):
        if self.available:
            self.available = False
            print(f'You have borrowed "{self.title}"')
        else:
            print('Book is already on loan.')

    def return_book(self):
        if not self.available:
            self.available = True
            print(f'You have returned "{self.title}"')
        else:
            print('Book is already available.')


# programa principal
book = Book('1984', 'George Orwell', 1949)
book.borrow_book()
print(book.available)
book.return_book()
print(book.available)