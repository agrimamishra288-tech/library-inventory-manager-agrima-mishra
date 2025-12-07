

from pathlib import Path
from typing import List, Optional
import logging

from .book import Book
from .storage import load_books, save_books, ensure_data_file

logger = logging.getLogger(__name__)

class LibraryInventory:
    def __init__(self, data_file: Optional[Path] = None):
        self.data_file = data_file or Path("books.json")
        ensure_data_file(self.data_file)
        self.books: List[Book] = load_books(self.data_file)

    def add_book(self, book: Book) -> bool:
        if any(b.isbn == book.isbn for b in self.books):
            logger.info("Attempt to add duplicate ISBN: %s", book.isbn)
            return False
        self.books.append(book)
        save_books(self.data_file, self.books)
        logger.info("Added book: %s", book.isbn)
        return True

    def find_by_isbn(self, isbn: str) -> Optional[Book]:
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def search_by_title(self, query: str) -> List[Book]:
        q = query.lower().strip()
        return [b for b in self.books if q in b.title.lower()]

    def issue_book(self, isbn: str) -> bool:
        book = self.find_by_isbn(isbn)
        if not book:
            logger.info("Issue failed. ISBN not found: %s", isbn)
            return False
        result = book.issue()
        if result:
            save_books(self.data_file, self.books)
            logger.info("Book issued: %s", isbn)
        else:
            logger.info("Book issue attempted but already issued: %s", isbn)
        return result

    def return_book(self, isbn: str) -> bool:
        book = self.find_by_isbn(isbn)
        if not book:
            logger.info("Return failed. ISBN not found: %s", isbn)
            return False
        result = book.return_book()
        if result:
            save_books(self.data_file, self.books)
            logger.info("Book returned: %s", isbn)
        else:
            logger.info("Return attempted but book was not issued: %s", isbn)
        return result

    def list_books(self) -> List[Book]:
        return list(self.books)
