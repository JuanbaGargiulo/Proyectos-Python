from book import Book
from menber import Member
from library import Library

# Create some book objects
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("Pride and Prejudice", "Jane Austen")

# Create a library object
library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Display all books in the library
library.display_books()

# Create a member object
member = Member("John Smith", "john@example.com")

# Member borrows a book
member.borrow_book(book1)

# Display book availability
library.display_books()

# Member returns the book
member.return_book(book1)

# Display book availability again
library.display_books()
