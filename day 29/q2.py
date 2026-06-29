arr = []

while True:
    print("\n--- Array Menu ---")
    print("1. Insert elements")
    print("2. Display array")
    print("3. Find sum")
    print("4. Find maximum")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        arr = list(map(int, input("Enter array elements: ").split()))
        print("Array created")

    elif choice == 2:
        print("Array:", arr)

    elif choice == 3:
        print("Sum:", sum(arr))

    elif choice == 4:
        if arr:
            print("Maximum:", max(arr))
        else:
            print("Array empty")

    elif choice == 5:
        break

    else:
        print("Invalid choice")