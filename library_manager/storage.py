
import json
from pathlib import Path
from typing import List
from .book import Book
import logging

logger = logging.getLogger(__name__)

def ensure_data_file(path: Path, default_books: List[Book] = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        logger.info("Data file not found. Creating default data file at %s", str(path))
        save_books(path, default_books or [])

def load_books(path: Path) -> List[Book]:
    try:
        if not path.exists():
            logger.info("Books file does not exist: %s", str(path))
            return []
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        books = [Book.from_dict(item) for item in data]
        logger.info("Loaded %d books from %s", len(books), str(path))
        return books
    except json.JSONDecodeError as e:
        logger.error("JSON decode error when reading %s: %s", str(path), e)
        return []
    except Exception as e:
        logger.exception("Unexpected error loading books: %s", e)
        return []

def save_books(path: Path, books: List[Book]) -> None:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as f:
            json.dump([b.to_dict() for b in books], f, indent=2, ensure_ascii=False)
        logger.info("Saved %d books to %s", len(books), str(path))
    except Exception as e:
        logger.exception("Error saving books to %s: %s", str(path), e)
