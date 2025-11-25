from library_manager.book import Book
from library_manager.inventory import LibraryInventory

def menu():
    inventory = LibraryInventory()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                title = input("Title: ")
                author = input("Author: ")
                isbn = input("ISBN: ")
                inventory.add_book(Book(title, author, isbn))
                print("Book added successfully!")

            elif choice == "2":
                isbn = input("Enter ISBN to issue: ")
                book = inventory.search_by_isbn(isbn)
                if book and book.issue():
                    inventory.save_books()
                    print("Book issued successfully!")
                else:
                    print("Book not available.")

            elif choice == "3":
                isbn = input("Enter ISBN to return: ")
                book = inventory.search_by_isbn(isbn)
                if book and book.return_book():
                    inventory.save_books()
                    print("Book returned successfully!")
                else:
                    print("Book not found or not issued.")

            elif choice == "4":
                for b in inventory.display_all():
                    print(b)

            elif choice == "5":
                title = input("Enter title keyword: ")
                results = inventory.search_by_title(title)
                for b in results:
                    print(b)

            elif choice == "6":
                print("Exiting...")
                break

            else:
                print("Invalid choice. Try again.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    menu()
