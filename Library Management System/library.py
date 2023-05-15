class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' by {book.author} has been added to the library.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Library Books:")
            for book in self.books:
                print(book)
