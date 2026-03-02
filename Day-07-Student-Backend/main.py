from app.data_manager import DataManager
from app.student_service import StudentService

data_manager = DataManager()
student_service = StudentService(data_manager)

def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. Get All Students")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            try:
                student_name = input("Enter student name: ")
                student_marks = int(input("Enter student marks: "))
                student_service.add_student(student_name, student_marks)
                print("Student added successfully.")
            except Exception as e:
                print(e)
        elif choice == "2":
            try:
                student_name = input("Enter student name to delete: ")
                student_service.delete_student(student_name)
                print("Student deleted successfully.")
            except Exception as e:
                print(e)
        elif choice == "3":
            try:
                student_name = input("Enter student name to update: ")
                new_marks = int(input("Enter new marks: "))
                student_service.update_marks(student_name, new_marks)
                print("Marks updated successfully.")
            except Exception as e:
                print(e)
        elif choice == "4":
            try:
                students = student_service.get_all_students()
                print("All Students:")
                for student in students:
                    print(f"Name: {student['name']}, Marks: {student['marks']}")
            except Exception as e:
                print(e)
        elif choice == "5":
            try:
                print("Exiting the program.")
                break
            except Exception as e:
                print(e)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()