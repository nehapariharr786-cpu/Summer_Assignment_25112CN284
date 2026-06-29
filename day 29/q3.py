string = ""

while True:
    print("\n--- String Menu ---")
    print("1. Enter String")
    print("2. Display String")
    print("3. Count characters")
    print("4. Reverse String")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        string = input("Enter string: ")

    elif choice == 2:
        print("String:", string)

    elif choice == 3:
        print("Length:", len(string))

    elif choice == 4:
        print("Reverse:", string[::-1])

    elif choice == 5:
        break

    else:
        print("Invalid choice")