class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        return f"Title: {self.title} | Author: {self.author} | Available: {'Yes' if self.available else 'No'}"
