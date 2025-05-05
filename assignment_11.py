class Book:
    total_books = 0  # Class variable to track the total number of books

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()  # Increment the book count when a new book is created

    @classmethod
    def increment_book_count(cls):
        # Class method to increment the total_books count
        cls.total_books += 1

    @classmethod
    def display_total_books(cls):
        # Class method to display the total number of books
        print(f"Total books: {cls.total_books}")

# Example usage
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")
book3 = Book("To Kill a Mockingbird", "Harper Lee")

# Display total books after adding some
Book.display_total_books()
