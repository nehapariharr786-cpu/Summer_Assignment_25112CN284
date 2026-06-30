books = []

def add_book():
    book_id = int(input("Enter Book ID: "))
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    books.append([book_id, title, author, "Available"])
    print("Book added successfully!")

def display_books():
    if not books:
        print("No books in library.")
    else:
        print("\nLibrary Books:")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Status: {book[3]}")

def issue_book():
    book_id = int(input("Enter Book ID to issue: "))

    for book in books:
        if book[0] == book_id:
            if book[3] == "Available":
                book[3] = "Issued"
                print("Book issued successfully!")
            else:
                print("Book is already issued.")
            return

    print("Book not found.")

def return_book():
    book_id = int(input("Enter Book ID to return: "))

    for book in books:
        if book[0] == book_id:
            if book[3] == "Issued":
                book[3] = "Available"
                print("Book returned successfully!")
            else:
                print("Book is already available.")
            return

    print("Book not found.")

while True:
    print("\n===== Mini Library System =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_book()

    elif choice == 2:
        display_books()

    elif choice == 3:
        issue_book()

    elif choice == 4:
        return_book()

    elif choice == 5:
        print("Exiting Library System...")
        break

    else:
        print("Invalid choice! Please try again.")