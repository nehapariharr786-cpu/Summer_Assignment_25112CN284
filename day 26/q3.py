balance = 5000

while True:
    print("\nATM MENU")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amount = int(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance -= amount
            print("Please collect your cash")
            print("Remaining Balance:", balance)
        else:
            print("Insufficient balance")

    elif choice == 3:
        amount = int(input("Enter deposit amount: "))
        balance += amount
        print("Amount deposited successfully")

    elif choice == 4:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")