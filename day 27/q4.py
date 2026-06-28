# Marksheet Generation System

students = []

def add_student():
    roll_no = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")

    math = int(input("Enter Maths Marks: "))
    science = int(input("Enter Science Marks: "))
    english = int(input("Enter English Marks: "))
    computer = int(input("Enter Computer Marks: "))

    total = math + science + english + computer
    percentage = total / 4

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "Fail"

    student = {
        "Roll No": roll_no,
        "Name": name,
        "Maths": math,
        "Science": science,
        "English": english,
        "Computer": computer,
        "Total": total,
        "Percentage": percentage,
        "Grade": grade
    }

    students.append(student)
    print("Marksheet Generated Successfully!\n")


def display_marksheet():
    if len(students) == 0:
        print("No records found\n")
    else:
        for s in students:
            print("----------------------------")
            print("Roll No:", s["Roll No"])
            print("Name:", s["Name"])
            print("Maths:", s["Maths"])
            print("Science:", s["Science"])
            print("English:", s["English"])
            print("Computer:", s["Computer"])
            print("Total Marks:", s["Total"])
            print("Percentage:", s["Percentage"], "%")
            print("Grade:", s["Grade"])
            print("----------------------------")


def search_student():
    roll = int(input("Enter Roll Number to search: "))

    for s in students:
        if s["Roll No"] == roll:
            print("Student Found")
            print(s)
            return

    print("Student not found")


while True:
    print("\nMarksheet Generation System")
    print("1. Generate Marksheet")
    print("2. Display Marksheet")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display_marksheet()

    elif choice == 3:
        search_student()

    elif choice == 4:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")