
# Name : Agrima Mishra
# Roll no.: 2501010207
# Assignment: 3

#LIBRARY INVENTORY 

class Book:
    def __init__(self, title, author, isbn, status="Available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def display_details(self):
        print("\nTitle :", self.title)
        print("Author:", self.author)
        print("ISBN  :", self.isbn)
        print("Status:", self.status)

    def issue_book(self):
        if self.status == "Available":
            self.status = "Issued"
            print(f"\nThe book '{self.title}' has been issued.")
        else:
            print(f"\nThe book '{self.title}' is unavailable.")

    def return_book(self):
        if self.status == "Issued":
            self.status = "Available"
            print(f"\nThe book '{self.title}' has been returned.")
        else:
            print(f"\nThe book '{self.title}' was not issued.")

    def save_to_file(self):
        try:
            with open("library.txt", "a") as f:
                f.write(f"{self.title},{self.author},{self.isbn},{self.status}\n")
            print("Book details saved!")
        except:
            print("Error writing to the file!")

def load_books():
    books = []
    try:
        with open("library.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line:
                    title, author, isbn, status = line.split(",")
                    books.append(Book(title, author, isbn, status))
    except FileNotFoundError:
        open("library.txt", "w").close()
    except:
        print("Error reading file.")
    return books

def update_file(books):
    try:
        with open("library.txt", "w") as f:
            for i in books:
                f.write(f"{i.title},{i.author},{i.isbn},{i.status}\n")
    except:
        print("Error updating file!")

def main():
    books = load_books()

    while True:
        print("\n==== LIBRARY MANAGEMENT SYSTEM ====")
        print("1. Add a new book")
        print("2. Display all books")
        print("3. Issue a book")
        print("4. Return a book")
        print("5. Exit")

        ch = input("\nEnter your choice: ")

        try:
            if ch == "1":
                title = input("\nEnter book title: ")
                author = input("Enter book author: ")
                isbn = input("Enter book ISBN: ")
                i = Book(title, author, isbn)
                books.append(i)
                i.save_to_file()

            elif ch == "2":
                print(f"\nTotal Books: {len(books)}")
                for i in books:
                    i.display_details()

            elif ch == "3":
                isbn = input("\nEnter ISBN to issue: ")
                found = False
                for i in books:
                    if i.isbn == isbn:
                        i.issue_book()
                        found = True
                        break
                if not found:
                    print("Book not found!")

            elif ch == "4":
                isbn = input("\nEnter ISBN to return: ")
                found = False
                for i in books:
                    if i.isbn == isbn:
                        i.return_book()
                        found = True
                        break
                if not found:
                    print("Book not found!")

            elif ch == "5":
                update_file(books)
                print("Program ending. All data saved.")
                break

            else:
                print("Invalid option! Please choose again.")

        except:
            print("An unexpected error occurred. Try again.")


main()
