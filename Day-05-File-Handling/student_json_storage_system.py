import json

STUDENT_FILE = "PYTHON BACK END/Day-05-File-Handling/student.json"

def _get_students():
    """Reads the list of students from the JSON file."""
    try:
        with open(STUDENT_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        # If file doesn't exist or is empty/corrupt, start with an empty list
        
        print("file not found")
        while True:
            print("\n1. create the file")
            print("2. exit")
            print(" ")
            choice = input("Enter your choice: ")
            if choice == '1':
                with open(STUDENT_FILE, 'x') as file:
                    json.dump([], file)
                print("File created successfully!")
                break
            elif choice == '2':
                print("Exiting the program.")
                exit()
            else:
                print("Invalid choice. Please try again.")

    except json.JSONDecodeError:
       return []

def add_student(student_data):
    """Adds a new student to the JSON file."""
    students = _get_students()
    students.append(student_data)
    with open(STUDENT_FILE, 'w') as file:
        json.dump(students, file, indent=4)
    print("Student added successfully!")

def view_students():
    """Displays all students from the JSON file."""
    students = _get_students()
    if not students:
        print("No students found.")
        return

    print("-" * 20)
    for student in students:
        print(f"Name: {student.get('name', 'N/A')}, Marks: {student.get('marks', 'N/A')}")
    print("-" * 20)

def main():
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            while True:
                try:
                    marks_input = input("Enter student marks: ")
                    marks = int(marks_input)
                    break
                except ValueError:
                    print("Invalid input. Please enter a number for marks.")
            
            student_data = {"name": name, "marks": marks}
            add_student(student_data)
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("Exiting the program.")
            break # Use break instead of exit() to allow for cleanup if needed
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()