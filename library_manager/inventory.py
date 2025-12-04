import json
from pathlib import Path
import logging
from .book import Book
from typing import List, Optional

logger = logging.getLogger(__name__)

class LibraryInventory:
    def __init__(self, json_path: str = "books.json"):
        self.json_path = Path(json_path)
        self.books: List[Book] = []
        self.load_from_file()

    def load_from_file(self):
        if not self.json_path.exists():
            logger.info("books.json not found, starting with empty inventory")
            self.books = []
            return

        try:
            data = json.loads(self.json_path.read_text(encoding="utf-8"))
            if not isinstance(data, list):
                raise ValueError("JSON root is not a list")
            self.books = [Book.from_dict(item) for item in data]
            logger.info(f"Loaded {len(self.books)} books from {self.json_path}")
        except Exception as e:
            logger.error("Failed to load books.json: %s", e)
            self.books = []

    def save_to_file(self):
        try:
            data = [b.to_dict() for b in self.books]
            self.json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
            logger.info("Saved books to books.json")
        except Exception as e:
            logger.error("Failed to save books.json: %s", e)

    def add_book(self, book: Book) -> bool:
        if any(b.isbn == book.isbn for b in self.books if b.isbn):
            logger.info("Book with isbn %s already exists", book.isbn)
            return False
        self.books.append(book)
        self.save_to_file()
        return True

    def search_by_title(self, title_substr: str) -> List[Book]:
        q = title_substr.strip().lower()
        return [b for b in self.books if q in b.title.lower()]

    def search_by_isbn(self, isbn: str) -> Optional[Book]:
        isbnq = str(isbn).strip()
        for b in self.books:
            if b.isbn == isbnq:
                return b
        return None

    def display_all(self) -> List[Book]:
        return list(self.books)

    def issue_book(self, isbn: str) -> bool:
        book = self.search_by_isbn(isbn)
        if not book:
            return False
        success = book.issue()
        if success:
            self.save_to_file()
        return success

    def return_book(self, isbn: str) -> bool:
        book = self.search_by_isbn(isbn)
        if not book:
            return False
        success = book.return_book()
        if success:
            self.save_to_file()
        return success
