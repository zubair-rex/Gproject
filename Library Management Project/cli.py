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
        library.save_library()
        pass

    elif choice == "2":
        # --- View Books ---
        print("===View options===")
        print("1.View all books")
        print("2.View books by Specific Genre")
        print("3.View books by availability")
        print("4.View borrowed books")
        options = input("Enter your option: ")

        if options == "1":
            print("----All Books----")
            library.view_books()

        elif options == "2":
            genre = input("Enter books genre: ").lower()
            print(f"----All Books in {genre} genre----")
            library.view_books(genre)

        elif options == "3":
            print("----All Available Books----")
            library.view_books(available=True)

        elif options == "4":  
            print("----All Borrowed Books----")
            library.view_books(available=False)
        else:
            print("Enter a valid option")
        
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
