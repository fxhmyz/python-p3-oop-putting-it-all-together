class Book:
    all_books = []

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        Book.all_books.append(self)

    def __repr__(self):
        return f"<Book: {self.title}, Author: {self.author}, Pages: {self.pages}>"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and value:
            self._title = value
        else:
            raise ValueError("Title must be a non-empty string.")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, str) and value:
            self._author = value
        else:
            raise ValueError("Author must be a non-empty string.")

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if isinstance(value, int) and value > 0:
            self._pages = value
        else:
            raise ValueError("Pages must be a positive integer.")

    @classmethod
    def get_all_books(cls):
        return cls.all_books
