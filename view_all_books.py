from load_books import load_books
def view_all_books():
    all_books = load_books("all_books.json")  # Load books from the JSON file
    if not all_books:  # Check if the list is empty
        print("No books found in the library.")
        return

    # Print table header
    print("Here are the books in the library:")
    print(
        f"{'Title':<15}{'Author':<15}{'ISBN':<10}{'Published':<12}{'Price':<8}{'Quantity':<10}"
    )
    print(
        f"{'-----':<15}{'------':<15}{'----':<10}{'---------':<12}{'-----':<8}{'-------':<10}"
    )

   
    for book in all_books:
        print(
            f"{book['title']:<15}{book['author']:<15}{book['isbn']:<10}{book['year']:<12}{book['price']:<8}{book['quantity']:<10}"
        )
