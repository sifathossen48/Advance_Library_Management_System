import json

def load_books(file_path="all_books.json"):
    with open(file_path, "r") as file:
        books = json.load(file)
    return books