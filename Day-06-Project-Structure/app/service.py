from app.data_manager import DataManager

class StudentService:
    """
    Provides business logic for managing students.
    It uses a DataManager instance to interact with the storage layer.
    """
    def __init__(self, data_manager: DataManager):
        self.manager = data_manager

    def add_student(self, student_data: dict):
        """Adds a new student."""
        students = self.manager.load_data()
        for student in students:
            if student["name"] == student_data["name"]:
                return "The Student already Exists"

        students.append(student_data)
        self.manager.save_data(students)
        return "Student added successfully!"

    def delete_student(self, student_name: str):
        """Deletes a student by name."""
        students = self.manager.load_data()
        original_count = len(students)
        students = [student for student in students if student.get("name") != student_name]
        
        if len(students) < original_count:
            self.manager.save_data(students)
            return f"Student '{student_name}' deleted successfully!"
        else:
            return f"Student '{student_name}' not found."

    def update_marks(self, student_name: str, new_marks: int):
        """Updates the marks for a specific student."""
        students = self.manager.load_data()
        student_found = False
        for student in students:
            if student.get("name") == student_name:
                student["marks"] = new_marks  # SOLVED: Assignment (=) instead of comparison (==)
                student_found = True
                break
        
        if student_found:
            self.manager.save_data(students)
            return f"Marks updated for '{student_name}'."
        else:
            return f"Student '{student_name}' not found."
