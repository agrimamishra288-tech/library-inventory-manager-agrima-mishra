import json

class Book:
    def __init__(self, title: str, author: str, isbn: str, status: str = "available"):
        self.title = title.strip()
        self.author = author.strip()
        self.isbn = str(isbn).strip()
        self.status = status.strip().lower()

    def __str__(self):
        return f"{self.title} | {self.author} | {self.isbn} | {self.status}"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status,
        }

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        if self.status == "issued":
            self.status = "available"
            return True
        return False

    def is_available(self):
        return self.status == "available"

    @staticmethod
    def from_dict(d):
        return Book(d.get("title", ""), d.get("author", ""), d.get("isbn", ""), d.get("status", "available"))
