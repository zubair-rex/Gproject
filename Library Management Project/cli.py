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
        print("--- Add Book ---")
        title = input("Enter books title:\n").lower()
        author = input("Enter books author name \n").lower()
        genre = input("Enter books genre \n").lower()
        book = Book(title, author, genre)
        library.add_book(book)
       
        library.save_library()
        pass

    elif choice == "2":
        print(" --- View Books ---")
        print("===View options===")
        print("1.View all books")
        print("2.View books by Specific Genre")
        print("3.View books by availability")
        print("4.View borrowed books")
        print("5.exit")
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
        elif options == "5":
            pass
        else:
            print("Enter a valid option")
        
        pass

    elif choice == "3":
        print("--- Borrow Book ---")
        title = input("Enter book title: ").lower()
        borrower_name = input("Enter borrower name: ").lower()
        borrow_date = datetime.date.today()
        library.borrow_book(title, borrower_name, borrow_date)
        
        library.save_library()
        pass

    elif choice == "4":
        print("--- Return Book ---")
        title = input("Enter your book title: ").lower()
        library.return_book(title)

        library.save_library()
        pass

    elif choice == "5":
        print("--- Search Book ---")

        title = input("Enter book title or few letters from title: ")
        print("Available books: \n")
        library.search_book(title)
        pass

    elif choice == "6":
        print("--- Delete Book ---")
        title = input("Enter book title you wanna delete: ").lower()
        library.delete_book(title)

        library.save_library()
        pass

    elif choice == "7":
        # --- Exit ---
        library.save_library()
        print("Exiting...")
        break

    else:
        print("Invalid choice, try again.")
