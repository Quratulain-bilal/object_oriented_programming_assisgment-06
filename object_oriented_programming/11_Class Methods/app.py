

# =============================================
# 11. Class Methods
# Create a class Book with a class variable total_books.
# Add a class method increment_book_count() to increase
# the count when a new book is added.
# =============================================

class Book:
    total_books = 0  # Class variable
    
    def __init__(self, title):
        self.title = title
        Book.increment_book_count()
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
    
    @classmethod
    def get_total_books(cls):
        return cls.total_books

# Test
b1 = Book("Python 101")
b2 = Book("OOP Principles")
print(Book.get_total_books())  # Output: 2
