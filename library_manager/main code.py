#NAME : Agrima Mishra
#ROLL NO. : 2501010207
#BTECH CSE
#DATE : 02/12/25

#DEINING DETAILS AND STATUS OF BOOKS 
class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def display_details(self):
        print(f"{self.title} by {self.author} (ISBN: {self.isbn}) - {self.status}")

    def issue_book(self):
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        if self.status == "issued":
            self.status = "available"
            return True
        return False


# SAVE DEATILS
def save_details(books, filename="books.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for book in books:
                line = f"{book.title}|{book.author}|{book.isbn}|{book.status}\n"
                f.write(line)
    except Exception as e:
        print(f"Error saving file {filename}: {e}")


# DEFINING LOAD BOOKS
def load_books(filename="books.txt"):
    books = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                title, author, isbn, status = line.strip().split("|")
                books.append(Book(title, author, isbn, status))
    except FileNotFoundError:
        
        books = [
            Book("1984", "George Orwell", "9780451524935"),
            Book("To Kill a Mockingbird", "Harper Lee", "9780061120084"),
            Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565"),
            Book("Pride and Prejudice", "Jane Austen", "9781503290563"),
        ]
        save_details(books, filename)
    except Exception as e:
        print(f"Error loading file {filename}: {e}")
    return books

# MAUN FUNCTIION 
def main():
    books = load_books()

    while True:
        print("\n1. Add Book 2. Issue Book 3. Return Book 4. Show All 5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter title: ").strip()
            author = input("Enter author: ").strip()
            isbn = input("Enter ISBN: ").strip()

            if not title or not author or not isbn:
                print("All fields are required.")
                continue

            if any(b.isbn == isbn for b in books):
                print("Book with this ISBN already exists.")
            else:
                books.append(Book(title, author, isbn))
                save_details(books)
                print("Book added.")

        elif choice == "2":
            print("Available books to issue:")
            for b in books:
                b.display_details()
            isbn = input("Enter ISBN to issue: ").strip()

            book_found = False
            for b in books:
                if b.isbn == isbn:
                    book_found = True
                    if b.issue_book():
                        save_details(books)
                        print("Book issued.")
                    else:
                        print("Book already issued.")
                    break
            if not book_found:
                print("Book not found.")

        elif choice == "3":
            print("Books currently issued:")
            issued_books = [b for b in books if b.status == "issued"]
            if not issued_books:
                print("No books are currently issued.")
            else:
                for b in issued_books:
                    b.display_details()
            isbn = input("Enter ISBN to return: ").strip()

            book_found = False
            for b in books:
                if b.isbn == isbn:
                    book_found = True
                    if b.return_book():
                        save_details(books)
                        print("Book returned.")
                    else:
                        print("Book already available.")
                    break
            if not book_found:
                print("Book not found.")

        elif choice == "4":
            if not books:
                print("No books available.")
            else:
                print("All books in library:")
                for b in books:
                    b.display_details()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
