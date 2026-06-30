students = []

def add_student():
    roll = int(input("Enter roll number: "))
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
    students.append([roll, name, marks])
    print("Student added successfully")

def display_students():
    for s in students:
        print("Roll:", s[0], "Name:", s[1], "Marks:", s[2])

def search_student():
    roll = int(input("Enter roll number: "))
    for s in students:
        if s[0] == roll:
            print("Student Found:", s)
            return
    print("Student not found")

while True:
    print("\n1.Add Student")
    print("2.Display Students")
    print("3.Search Student")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        display_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        break
    else:
        print("Invalid choice")