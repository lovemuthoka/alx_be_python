class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                return f"{title} has been checked out."
        return f"{title} is not available."

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                return f"{title} has been returned."
        return f"{title} was not checked out."

    def list_available_books(self):
        available_books = [book for book in self._books if not book._is_checked_out]
        if not available_books:
            return "No books are currently available."
        return "\n".join(f"{book.title} by {book.author}" for book in available_books)

if __name__ == "__main__":
