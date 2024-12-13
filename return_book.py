import save_all_books
import json

def return_book(all_books, book_id, borrower_name):
  
    book_id = int(book_id)

    
    try:
        with open("lending_info.json", "r") as file:
            lending_records = json.load(file) 
    except FileNotFoundError:
        print("Lending information file not found.")
        return
    except json.JSONDecodeError:
        print("Error decoding the JSON in lending_info.json.")
        return

    updated_records = []
    is_returned = False
    book_found = False

    for lending_info in lending_records:


        if int(lending_info['isbn']) == book_id: 
            book_found = True
            if lending_info['borrower_name'].lower() == borrower_name.lower():  
                is_returned = True
                print(f"Book titled '{lending_info['book_title']}' returned by {lending_info['borrower_name']}.")
            else:
                updated_records.append(lending_info)
        else:
            updated_records.append(lending_info)

    if book_found:
        if is_returned:
       
            with open("lending_info.json", "w") as file:
                json.dump(updated_records, file, indent=4)

            for book in all_books:
                if int(book['isbn']) == book_id:
                    book['quantity'] = int(book['quantity']) + 1
                    save_all_books.save_all__books(all_books)
                    break
        else:
            print(f"No record of this book being lent to {borrower_name}.")
    else:
        print(f"Book with ISBN {book_id} not found.")
