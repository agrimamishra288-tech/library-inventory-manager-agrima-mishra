import logging
from pathlib import Path
from library_manager.inventory import LibraryInventory
from library_manager.book import Book

# simple logging setup
LOG_PATH = Path("library.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def input_non_empty(prompt):
    while True:
        v = input(prompt).strip()
        if v:
            return v
        print("Please enter a value")

def print_menu():
    print()
    print("Library Inventory Manager")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search by Title")
    print("6. Search by ISBN")
    print("7. Save Catalog")
    print("8. Exit")
    print()

def add_book_flow(inv: LibraryInventory):
    try:
        title = input_non_empty("Title: ")
        author = input_non_empty("Author: ")
        isbn = input_non_empty("ISBN: ")
        book = Book(title=title, author=author, isbn=isbn)
        inv.add_book(book)
        print("Book added.")
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        logger.exception("Unexpected error adding book")
        print("Failed to add book.")

def issue_book_flow(inv: LibraryInventory):
    isbn = input_non_empty("Enter ISBN to issue: ")
    try:
        inv.issue_book(isbn)
        print("Book issued.")
    except LookupError:
        print("Book not found.")
    except RuntimeError as e:
        print("Cannot issue:", e)
    except Exception:
        logger.exception("Unexpected error issuing book")
        print("Failed to issue book.")

def return_book_flow(inv: LibraryInventory):
    isbn = input_non_empty("Enter ISBN to return: ")
    try:
        inv.return_book(isbn)
        print("Book returned.")
    except LookupError:
        print("Book not found.")
    except RuntimeError as e:
        print("Cannot return:", e)
    except Exception:
        logger.exception("Unexpected error returning book")
        print("Failed to return book.")

def view_all_flow(inv: LibraryInventory):
    books = inv.display_all()
    if not books:
        print("No books in catalog.")
        return
    print()
    print(f"{'Title':40} {'Author':25} {'ISBN':15} {'Status'}")
    print("-" * 95)
    for b in books:
        print(f"{b.title[:38]:40} {b.author[:23]:25} {b.isbn:15} {b.status}")
    print("-" * 95)

def search_title_flow(inv: LibraryInventory):
    q = input_non_empty("Enter title search text: ")
    results = inv.search_by_title(q)
    if not results:
        print("No books found.")
        return
    for b in results:
        print(b)

def search_isbn_flow(inv: LibraryInventory):
    isbn = input_non_empty("Enter ISBN: ")
    b = inv.search_by_isbn(isbn)
    if not b:
        print("No book with that ISBN.")
        return
    print(b)

def main():
    inv = LibraryInventory(json_path="catalog.json")
    while True:
        print_menu()
        choice = input("Enter choice (1-8): ").strip()
        if choice == "1":
            add_book_flow(inv)
        elif choice == "2":
            issue_book_flow(inv)
        elif choice == "3":
            return_book_flow(inv)
        elif choice == "4":
            view_all_flow(inv)
        elif choice == "5":
            search_title_flow(inv)
        elif choice == "6":
            search_isbn_flow(inv)
        elif choice == "7":
            try:
                inv.save_to_file()
                print("Catalog saved.")
            except Exception:
                print("Failed to save catalog. See log.")
        elif choice == "8":
            # save before exit
            try:
                inv.save_to_file()
                print("Catalog saved. Exiting.")
            except Exception:
                print("Could not save catalog. Exiting anyway.")
            break
        else:
            print("Please enter a number between 1 and 8")

if __name__ == "__main__":
    main()
