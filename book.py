class Book:
    """Represents a single book in the library"""
    def __init__(self, title: str, author: str, isbn: str, is_borrowed: bool = False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = is_borrowed

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
