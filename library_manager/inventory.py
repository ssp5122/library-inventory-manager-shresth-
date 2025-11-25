import json
import logging
from pathlib import Path
from .book import Book

logging.basicConfig(filename="library.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

class LibraryInventory:
    def __init__(self, file_path="catalog.json"):
        self.books = []
        self.file_path = Path(file_path)
        self.load_books()

    def add_book(self, book):
        self.books.append(book)
        logging.info(f"Book added: {book.title}")
        self.save_books()

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        return next((b for b in self.books if b.isbn == isbn), None)

    def display_all(self):
        return [str(b) for b in self.books]

    def save_books(self):
        try:
            with open(self.file_path, "w") as f:
                json.dump([b.to_dict() for b in self.books], f, indent=4)
        except Exception as e:
            logging.error(f"Error saving books: {e}")

    def load_books(self):
        try:
            if self.file_path.exists():
                with open(self.file_path, "r") as f:
                    data = json.load(f)
                    self.books = [Book(**d) for d in data]
        except Exception as e:
            logging.error(f"Error loading books: {e}")
