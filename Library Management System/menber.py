
class Member:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.borrowed_books = []

    def __str__(self):
        return f"Name: {self.name} | Contact: {self.contact}"

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            print(f"{self.name} has borrowed the book: {book.title}")
        else:
            print("Sorry, the book is currently not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            print(f"{self.name} has returned the book: {book.title}")
        else:
            print("You have not borrowed this book.")
