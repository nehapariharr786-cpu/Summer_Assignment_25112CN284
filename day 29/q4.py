inventory = {}

while True:
    print("\n--- Inventory Menu ---")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Quantity")
    print("4. Remove Product")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter product name: ")
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        inventory[name] = {
            "quantity": qty,
            "price": price
        }

        print("Product added")

    elif choice == 2:
        for name, details in inventory.items():
            print(name, details)

    elif choice == 3:
        name = input("Enter product name: ")

        if name in inventory:
            qty = int(input("Enter new quantity: "))
            inventory[name]["quantity"] = qty
            print("Updated")
        else:
            print("Product not found")

    elif choice == 4:
        name = input("Enter product name: ")

        if name in inventory:
            del inventory[name]
            print("Removed")
        else:
            print("Product not found")

    elif choice == 5:
        break

    else:
        print("Invalid choice")