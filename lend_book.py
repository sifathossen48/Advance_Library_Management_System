import datetime

import save_all_books

def lend_book(all_books, book_id):

    book_id = str(book_id)

    for book in all_books:
        if book['isbn'] == book_id:
            if int(book['quantity']) > 0:
                # Ask for borrower's information
                borrower_name = input("Enter borrower's name: ").strip()
                borrower_phone = input("Enter borrower's phone number: ").strip()
                return_due_date = input("Enter return due date (YYYY-MM-DD): ").strip()

                # Validate date format
                try:
                    return_due_date = datetime.strptime(return_due_date, "%Y-%m-%d").date()
                except ValueError:
                    print("Invalid date format.")
                    return all_books

                # Update book information
                book['quantity'] = str(int(book['quantity']) - 1)
                book['borrower_name'] = borrower_name
                book['borrower_phone'] = borrower_phone
                book['return_due_date'] = str(return_due_date)

                print(f"Book lent successfully to {borrower_name}. Due back on {return_due_date}.")
                return all_books

    print("Book not found.")
    return all_books
