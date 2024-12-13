import add_books
import save_all_books
import view_all_books
import restore_books_file
from datetime import datetime
import update_book_file, delete_book_file
import lend_book
import load_books
import return_book


all_books = load_books.load_books()


while True:
    print("Welcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Book Update")
    print("4. Book Remove/Delete")
    print("5. Lend a Book")
    print("6. Return a Book")


    menu = input("Select any number: ")
    
    if menu == "0":
        print("Thanks for using Library Management System ")
        break
    elif menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        if not all_books:
            print("No books available")
        else:
            view_all_books.view_all_books()
    elif menu == "3":
        update_book_file.update_books(all_books)
    elif menu == "4":
        delete_book_file.delete_books(all_books)
    elif menu == "5":
        view_all_books.view_all_books()
        book_id = int(input('Enter ISBN number of the book you want to lend: '))
        lend_book.lend_book(all_books,book_id)
    elif menu =="6":
        view_all_books.view_all_books()  # Show the list of books
        book_id = int(input('Enter ISBN number of the book you want to return: '))  # Convert to int
        borrower_name = input('Enter the name of the borrower: ')
        return_book.return_book(all_books, book_id, borrower_name)

    else:
        print("Choose a valid number")