from app.database import DataBase
from app.student_service import StudentService
import sqlite3

service = StudentService()

while True:
    print("\n1. Add student\n2. Delete student\n3. Update marks\n4. Get all students\n5. Exit")
    choice = input("Enter your choice: ")
    try:
        if choice == "1":
            name = input("Enter student name: ")
            marks = int(input("Enter student marks: "))
            print(service.add_student(name, marks))
        elif choice == "2":
            name = input("Enter student name: ")
            print(service.delete_student(name))
        elif choice == "3":
            name = input("Enter student name: ")
            marks = int(input("Enter new marks: "))
            print(service.update_marks(name, marks))
        elif choice == "4":
            students =service.get_all_students()
            for student in students:
                print(student)

        elif choice == "5":
            break
        else:
            print("Invalid choice")
    except ValueError as e:
        print(e)
