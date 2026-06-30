employees = []

def add_employee():
    emp_id = int(input("Enter employee id: "))
    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))

    employees.append([emp_id, name, salary])
    print("Employee added")

def show_employee():
    for e in employees:
        print("ID:", e[0], "Name:", e[1], "Salary:", e[2])

def search_employee():
    emp_id = int(input("Enter employee id: "))

    for e in employees:
        if e[0] == emp_id:
            print("Employee Found:", e)
            return

    print("Employee not found")


while True:
    print("\n--- Employee Management ---")
    print("1.Add Employee")
    print("2.Display Employee")
    print("3.Search Employee")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_employee()
    elif choice == 2:
        show_employee()
    elif choice == 3:
        search_employee()
    elif choice == 4:
        break
    else:
        print("Invalid choice")