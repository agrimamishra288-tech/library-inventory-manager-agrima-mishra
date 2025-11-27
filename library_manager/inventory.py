import json
from pathlib import Path
import logging
from .book import Book

logger = logging.getLogger(__name__)

class LibraryInventory:
    def __init__(self, json_path="catalog.json"):
        self.books = []  # list of Book objects
        self.json_path = Path(json_path)
        # try load existing catalog
        try:
            self.load_from_file()
        except Exception as e:
            logger.info("Starting with empty catalog: %s", e)

    def add_book(self, book: Book):
        # prevent duplicate isbn
        if self.search_by_isbn(book.isbn):
            logger.error("Book with ISBN %s already exists", book.isbn)
            raise ValueError("ISBN already exists in catalog")
        self.books.append(book)
        logger.info("Added book %s", book.isbn)

    def search_by_title(self, title_substring):
        title_substring = title_substring.lower()
        return [b for b in self.books if title_substring in b.title.lower()]

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        return list(self.books)  # return copy

    def issue_book(self, isbn):
        b = self.search_by_isbn(isbn)
        if not b:
            logger.error("Issue failed. ISBN %s not found", isbn)
            raise LookupError("Book not found")
        if not b.issue():
            logger.error("Issue failed. Book %s already issued", isbn)
            raise RuntimeError("Book already issued")
        logger.info("Issued book %s", isbn)
        return True

    def return_book(self, isbn):
        b = self.search_by_isbn(isbn)
        if not b:
            logger.error("Return failed. ISBN %s not found", isbn)
            raise LookupError("Book not found")
        if not b.return_book():
            logger.error("Return failed. Book %s already available", isbn)
            raise RuntimeError("Book already available")
        logger.info("Returned book %s", isbn)
        return True

    def save_to_file(self):
        try:
            data = [book.to_dict() for book in self.books]
            with self.json_path.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            logger.info("Catalog saved to %s", self.json_path)
        except Exception as e:
            logger.error("Failed to save catalog: %s", e)
            raise

    def load_from_file(self):
        if not self.json_path.exists():
            logger.info("Catalog file %s does not exist, nothing to load", self.json_path)
            return
        try:
            with self.json_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
            self.books = [Book.from_dict(d) for d in data]
            logger.info("Loaded %d books from %s", len(self.books), self.json_path)
        except json.JSONDecodeError:
            logger.error("Catalog file is corrupted or not valid JSON")
            raise
        except Exception as e:
            logger.error("Unexpected error loading catalog: %s", e)
            raise
