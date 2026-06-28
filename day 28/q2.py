accounts = {}

def create_account():
    acc = int(input("Enter Account Number: "))
    name = input("Enter Name: ")
    balance = float(input("Enter Initial Balance: "))

    accounts[acc] = {
        "Name": name,
        "Balance": balance
    }

    print("Account Created Successfully")


def deposit():
    acc = int(input("Enter Account Number: "))
    amount = float(input("Enter Deposit Amount: "))

    accounts[acc]["Balance"] += amount
    print("Money Deposited")


def withdraw():
    acc = int(input("Enter Account Number: "))
    amount = float(input("Enter Withdraw Amount: "))

    if accounts[acc]["Balance"] >= amount:
        accounts[acc]["Balance"] -= amount
        print("Withdrawal Successful")
    else:
        print("Insufficient Balance")


def display():
    print(accounts)


while True:
    print("\nBank Account System")
    print("1.Create Account")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Display")
    print("5.Exit")

    ch=int(input("Choice: "))

    if ch==1:
        create_account()
    elif ch==2:
        deposit()
    elif ch==3:
        withdraw()
    elif ch==4:
        display()
    else:
        break