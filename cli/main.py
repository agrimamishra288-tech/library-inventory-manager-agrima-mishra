import logging
from library_manager.inventory import LibraryInventory
from library_manager.book import Book

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def print_menu():
    print()
    print("Library Inventory")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")

def safe_input(prompt):
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print()
        return ""

def add_book_cli(inv: LibraryInventory):
    print("\nAdd book (leave title empty to cancel)")
    title = safe_input("Title: ").strip()
    if not title:
        print("Canceling.")
        return
    author = safe_input("Author: ").strip() or "Unknown"
    isbn = safe_input("ISBN: ").strip() or ""
    book = Book(title, author, isbn, "available")
    ok = inv.add_book(book)
    if ok:
        print("Book added.")
    else:
        print("Book not added. ISBN may already exist.")

def issue_book_cli(inv: LibraryInventory):
    isbn = safe_input("Enter ISBN to issue: ").strip()
    if not isbn:
        print("Empty ISBN.")
        return
    ok = inv.issue_book(isbn)
    if ok:
        print("Book issued.")
    else:
        print("Could not issue. Either not found or already issued.")

def return_book_cli(inv: LibraryInventory):
    isbn = safe_input("Enter ISBN to return: ").strip()
    if not isbn:
        print("Empty ISBN.")
        return
    ok = inv.return_book(isbn)
    if ok:
        print("Book returned.")
    else:
        print("Could not return. Either not found or already available.")

def view_all_cli(inv: LibraryInventory):
    books = inv.display_all()
    if not books:
        print("No books in inventory.")
        return
    print("\nAll books:")
    for b in books:
        print(b)

def search_cli(inv: LibraryInventory):
    print("\nSearch by")
    print("1. Title")
    print("2. ISBN")
    choice = safe_input("Choose 1 or 2: ").strip()
    if choice == "1":
        q = safe_input("Title or part of title: ").strip()
        results = inv.search_by_title(q)
        if not results:
            print("No matches.")
        else:
            for b in results:
                print(b)
    elif choice == "2":
        q = safe_input("ISBN: ").strip()
        b = inv.search_by_isbn(q)
        if b:
            print(b)
        else:
            print("No book with that ISBN.")
    else:
        print("Invalid choice.")

def main():
    inv = LibraryInventory("books.json")
    while True:
        print_menu()
        choice = safe_input("Choose an option: ").strip()
        if choice == "1":
            add_book_cli(inv)
        elif choice == "2":
            issue_book_cli(inv)
        elif choice == "3":
            return_book_cli(inv)
        elif choice == "4":
            view_all_cli(inv)
        elif choice == "5":
            search_cli(inv)
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
