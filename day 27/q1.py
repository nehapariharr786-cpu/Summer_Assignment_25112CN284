students = []

while True:
    print("\n--- Student Record Management System ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

        student = {
            "Roll": roll,
            "Name": name,
            "Age": age,
            "Marks": marks
        }

        students.append(student)
        print("Student added successfully")

    elif choice == 2:
        if len(students) == 0:
            print("No records found")
        else:
            for s in students:
                print(s)

    elif choice == 3:
        roll = int(input("Enter Roll No to search: "))

        found = False
        for s in students:
            if s["Roll"] == roll:
                print("Student Found:", s)
                found = True

        if not found:
            print("Student not found")

    elif choice == 4:
        roll = int(input("Enter Roll No to delete: "))

        for s in students:
            if s["Roll"] == roll:
                students.remove(s)
                print("Record deleted")
                break
        else:
            print("Student not found")

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice")