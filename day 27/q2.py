employees = []

while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        employee = {
            "ID": emp_id,
            "Name": name,
            "Department": department,
            "Salary": salary
        }

        employees.append(employee)
        print("Employee added successfully")

    elif choice == 2:
        if len(employees) == 0:
            print("No employee records")
        else:
            for e in employees:
                print(e)

    elif choice == 3:
        emp_id = int(input("Enter Employee ID to search: "))

        found = False
        for e in employees:
            if e["ID"] == emp_id:
                print("Employee Found:", e)
                found = True

        if not found:
            print("Employee not found")

    elif choice == 4:
        emp_id = int(input("Enter Employee ID to delete: "))

        for e in employees:
            if e["ID"] == emp_id:
                employees.remove(e)
                print("Employee deleted")
                break
        else:
            print("Employee not found")

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice")