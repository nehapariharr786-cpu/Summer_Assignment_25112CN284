contacts = {}

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")

    contacts[name] = phone
    print("Contact Saved")


def search_contact():
    name = input("Enter Name: ")

    if name in contacts:
        print("Phone:", contacts[name])
    else:
        print("Contact Not Found")


def delete_contact():
    name = input("Enter Name: ")

    if name in contacts:
        del contacts[name]
        print("Contact Deleted")
    else:
        print("Contact Not Found")


while True:
    print("\nContact Management System")
    print("1.Add Contact")
    print("2.Search Contact")
    print("3.Delete Contact")
    print("4.Exit")

    ch=int(input("Choice: "))

    if ch==1:
        add_contact()
    elif ch==2:
        search_contact()
    elif ch==3:
        delete_contact()
    else:
        break