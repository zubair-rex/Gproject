import json
import datetime


class Book:
    def __init__(self, title, author, genre, is_available=True, borrower_name=None, borrow_date=None):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_available = is_available
        self.borrower_name = borrower_name
        self.borrow_date = borrow_date

    #convert book to dict for json
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "is_available": self.is_available,
            "borrower_name": self.borrower_name,
            "borrow_date": self.borrow_date.strftime("%Y-%m-%d") if self.borrow_date else None
        }

    #classmethod to create book from dic
    @classmethod
    def from_dict(cls, data):
        title = data["title"]
        author = data["author"]
        genre = data["genre"]
        is_available = data["is_available"]
        borrower_name = data["borrower_name"]
        borrow_date = data["borrow_date"]

        book = cls(title, author, genre, is_available, borrower_name, borrow_date)
        return book
 


    #update availability, borrower, borrow_date
    def borrow(self, borrower_name, borrow_date):
        if self.is_available:
            self.is_available = False
            self.borrower_name = borrower_name
            self.borrow_date = borrow_date
        else:
            print(f"{self.title} is already borrowed")


    #reset availability, borrower, borrow_date
    def return_book(self):
        self.is_available = True
        self.borrower_name = None
        self.borrow_date = None



class Library:
    def __init__(self):
        self.books = []

    #add book object to list
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully!")

    #remove book by title
    def delete_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Book '{title}' removed successfully!")
                return
        print(f"No book with title '{title}' found.")

    #mark a book borrowed,, save borrowe/date
    def borrow_book(self, title, borrower_name, borrow_date):
        for book in self.books:
            if book.title == title:
                if book.is_available:
                    book.borrow(borrower_name, borrow_date)
                    print(f"You borrowed '{book.title}' successfully!")
                else:
                    print(f"Sorry, '{book.title}' is already borrowed by {book.borrower_name}.")
                return
    
    #mark a book returned
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                print(f"You've succesfully returned {book.title} book")
                return
        
        print(f"{title} was not found")
        

    #by title, author, genre
    def search_book(self, name):
        foud = False
        for book in self.books:
            if name in book.title:
                print(book.title)
                foud = True
        if not foud:
            print(f"we didn't found {name}")
    
    #show all books, filter by genre/availablity
    def view_books(self, genre=None, available=None):
        found = False
        for book in self.books:
            if genre == None and available == None:
                print(f"Name: {book.title} | Author: {book.author} | Genre: {book.genre} | Available: {book.is_available}")
                found = True
            if genre is not None and book.genre == genre:
                print(f"Name: {book.title} | Author: {book.author} | Genre: {book.genre} | Availbale: {book.is_available}")
                found = True
            if available is not None and available == book.is_available:
                print(f"Name: {book.title} | Author: {book.author} | Genre: {book.genre}")
                found = True
        if not found: 
            print("No books were found in this filter")


    #write list of books to JSON
    def save_library(self):
        data = []
        for book in self.books:
            data.append(book.to_dict())

        with open("library.json", "w") as f:
            json.dump(data, f, indent=4)

            

    #read books from JSON, conver to Book objects
    def load_library(self):
        try:
            with open("library.json", "r") as f:
                data = json.load(f)

                self.books = []

                for book_dict in data:
                    book = Book.from_dict(book_dict)
                    self.books.append(book)
                print("Library loaded successfully")
        except FileNotFoundError:
            self.books = []

            print("No Library found, starting with an empty library") 