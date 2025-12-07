

import logging
from pathlib import Path
from library_manager import Book, LibraryInventory

LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s %(message)s"

def setup_logging(log_path: Path = Path("library.log")):
    logging.basicConfig(
        level=logging.INFO,
        format=LOG_FORMAT,
        handlers=[
            logging.FileHandler(log_path, encoding="utf-8"),
            logging.StreamHandler()
        ]
    )

def prompt(msg: str) -> str:
    return input(msg).strip()

def main():
    setup_logging()
    logger = logging.getLogger("cli")
    logger.info("Starting Library Inventory CLI")

    data_file = Path("books.json")
    inventory = LibraryInventory(data_file)

    while True:
        print("\n1. Add Book  2. Issue Book  3. Return Book  4. Show All  5. Search by Title  6. Exit")
        choice = prompt("Enter your choice: ")

        if choice == "1":
            title = prompt("Enter title: ")
            author = prompt("Enter author: ")
            isbn = prompt("Enter ISBN: ")

            if not title or not author or not isbn:
                print("All fields are required.")
                continue

            book = Book(title=title, author=author, isbn=isbn)
            if inventory.add_book(book):
                print("Book added.")
            else:
                print("Book with this ISBN already exists.")

        elif choice == "2":
            isbn = prompt("Enter ISBN to issue: ")
            if inventory.issue_book(isbn):
                print("Book issued.")
            else:
                print("Could not issue book. Check ISBN or book status.")

        elif choice == "3":
            isbn = prompt("Enter ISBN to return: ")
            if inventory.return_book(isbn):
                print("Book returned.")
            else:
                print("Could not return book. Check ISBN or book status.")

        elif choice == "4":
            books = inventory.list_books()
            if not books:
                print("No books in the library.")
            else:
                print("All books in library:")
                for b in books:
                    print(str(b))

        elif choice == "5":
            q = prompt("Enter title search query: ")
            results = inventory.search_by_title(q)
            if results:
                for b in results:
                    print(str(b))
            else:
                print("No books found matching that title.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
