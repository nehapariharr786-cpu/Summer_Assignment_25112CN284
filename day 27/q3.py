# Salary Management System

employees = []

def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Basic Salary: "))

    hra = salary * 0.20
    da = salary * 0.10
    tax = salary * 0.05

    net_salary = salary + hra + da - tax

    employee = {
        "ID": emp_id,
        "Name": name,
        "Basic Salary": salary,
        "HRA": hra,
        "DA": da,
        "Tax": tax,
        "Net Salary": net_salary
    }

    employees.append(employee)
    print("Employee added successfully!\n")


def display_salary():
    if len(employees) == 0:
        print("No employee records found\n")
    else:
        for emp in employees:
            print("----------------------")
            print("Employee ID:", emp["ID"])
            print("Name:", emp["Name"])
            print("Basic Salary:", emp["Basic Salary"])
            print("HRA:", emp["HRA"])
            print("DA:", emp["DA"])
            print("Tax:", emp["Tax"])
            print("Net Salary:", emp["Net Salary"])
            print("----------------------")


def search_employee():
    eid = int(input("Enter Employee ID to search: "))

    for emp in employees:
        if emp["ID"] == eid:
            print("Employee Found")
            print(emp)
            return

    print("Employee not found")


while True:
    print("\nSalary Management System")
    print("1. Add Employee")
    print("2. Display Salary Details")
    print("3. Search Employee")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_employee()

    elif choice == 2:
        display_salary()

    elif choice == 3:
        search_employee()

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")