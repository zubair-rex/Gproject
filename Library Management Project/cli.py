import datetime

from models import Book, Library

library = Library()
library.load_library()

# --- CLI Loop ---
while True:
    print("\n=== Library Menu ===")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        # --- Add Book ---
        # get input from user: title, author, genre
        title = input("Enter books title:\n").lower()
        author = input("Enter books author name \n").lower()
        genre = input("Enter books genre \n").lower()
        # create Book object
        book = Book(title, author, genre)
        # call library.add_book(book)
        library.add_book(book)
        # call library.save_library()
        library.save_library(book)
        pass

    elif choice == "2":
        # --- View Books ---
        # optional: get genre filter from user
        # optional: get availability filter (y/n) from user
        # call library.view_books(genre=..., available=...)
        pass

    elif choice == "3":
        # --- Borrow Book ---
        # get input: title, borrower_name
        # get borrow_date as datetime.date.today()
        # call library.borrow_book(title, borrower_name, borrow_date)
        # call library.save_library()
        pass

    elif choice == "4":
        # --- Return Book ---
        # get input: title
        # call library.return_book(title)
        # call library.save_library()
        pass

    elif choice == "5":
        # --- Search Book ---
        # get input: search string (title, author, or genre)
        # call library.search_book(search_string)
        pass

    elif choice == "6":
        # --- Delete Book ---
        # get input: title
        # call library.delete_book(title)
        # call library.save_library()
        pass

    elif choice == "7":
        # --- Exit ---
        library.save_library()
        print("Exiting...")
        break

    else:
        print("Invalid choice, try again.")
