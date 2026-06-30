books = []

def add_book():
    book_id = int(input("Enter book id: "))
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    books.append([book_id, title, author, "Available"])
    print("Book added successfully")


def display_books():
    if len(books) == 0:
        print("No books available")
    else:
        for b in books:
            print(b)


def issue_book():
    book_id = int(input("Enter book id: "))

    for b in books:
        if b[0] == book_id:
            if b[3] == "Available":
                b[3] = "Issued"
                print("Book issued")
            else:
                print("Book already issued")
            return

    print("Book not found")


def return_book():
    book_id = int(input("Enter book id: "))

    for b in books:
        if b[0] == book_id:
            b[3] = "Available"
            print("Book returned")
            return

    print("Book not found")


while True:
    print("\n--- Library Management System ---")
    print("1.Add Book")
    print("2.Display Books")
    print("3.Issue Book")
    print("4.Return Book")
    print("5.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_book()

    elif choice == 2:
        display_books()

    elif choice == 3:
        issue_book()

    elif choice == 4:
        return_book()

    elif choice == 5:
        break

    else:
        print("Invalid choice")