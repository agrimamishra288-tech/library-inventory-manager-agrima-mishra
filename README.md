Name : Agrima Mishra

Roll no: 2501010207

Lab Assignment 3

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Library Inventory Manager

This is a small python project where I made a simple library inventory system using classes, json file storage, logging and a menu based cli. it was built for my programming assignment to understand oop concepts and how to organize a python project into folders.

the program helps add books, issue them, return them and keep everything saved in a json file so the data stays even after closing.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Screenshots of the output 

<img width="806" height="201" alt="Screenshot 2025-12-07 145635" src="https://github.com/user-attachments/assets/c134121b-c996-4deb-b5fe-b2c20f8efac6" />


<img width="833" height="761" alt="Screenshot 2025-12-07 151801" src="https://github.com/user-attachments/assets/7829a1d1-b0ce-4384-8464-23f754438aa1" />

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## features

- add new books with title, author and isbn

- issue a book if it is available

- return a previously issued book

- search books by title

- view all books in the system

- books are saved inside a books.json file

- logs every action into library.log

- uses proper folders and modules for cleaner structure

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# How it Works ?

## book class

each book has

- title

- author

- isbn

- status (available or issued)

- plus small methods to issue, return and convert to dictionary.


## inventory

handles

- adding books

- checking duplicates

- issuing and returning

- searching by title

- saving and loading from json

- file storage

data is stored inside books.json

the project uses pathlib for file paths and handles missing files safely.

## logging

all actions like adding or issuing books are recorded in library.log automatically.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# how to run

1). open terminal inside the project folder

 run:

 python -m cli.main


or if your system uses py:

py -m cli.main


the menu will appear:

1. Add Book
   
2. Issue Book

3. Return Book

4. Show All

5. Search by Title

6. Exit


just type the number and follow the options.

books.json example
[

  {
  
    "title": "1984",
    
    "author": "George Orwell",
    
    "isbn": "9780451524935",
    
    "status": "available"
    
  }
  
]


the file updates by itself whenever a book is added, issued or returned.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# What I Learned 

- how to split code into multiple python files

- how classes and objects make code cleaner

- using json instead of text to store data

- logging and debugging

- how python modules work with folders

