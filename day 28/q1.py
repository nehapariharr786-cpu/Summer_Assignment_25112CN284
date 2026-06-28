

books = []

def add_book():
    book_id = int(input("Enter Book ID: "))
    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    book = {
        "ID": book_id,
        "Name": name,
        "Author": author,
        "Status": "Available"
    }

    books.append(book)
    print("Book Added Successfully\n")


def issue_book():
    bid = int(input("Enter Book ID: "))

    for b in books:
        if b["ID"] == bid and b["Status"] == "Available":
            b["Status"] = "Issued"
            print("Book Issued Successfully")
            return

    print("Book not available")


def display_books():
    for b in books:
        print(b)


while True:
    print("\nLibrary Management System")
    print("1.Add Book")
    print("2.Issue Book")
    print("3.Display Books")
    print("4.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        add_book()
    elif ch == 2:
        issue_book()
    elif ch == 3:
        display_books()
    elif ch == 4:
        break