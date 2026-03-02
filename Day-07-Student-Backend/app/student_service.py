from app.data_manager import DataManager
from app.exceptions import DuplicateStudentError, StudentNotFoundError, InvalidMarksError

# data_manager = DataManager()

class StudentService():
    def __init__(self, data_manager):
        self.data_manager = data_manager

    def add_student(self, student_name, student_marks):
        students = self.data_manager.load_data()
        if student_marks < 0 or student_marks > 100:
            raise InvalidMarksError("Invalid marks. Marks should be between 0 and 100.")
        else:
            student_data = {"name": student_name, "marks": student_marks}
            for student in students:
                if student["name"] == student_name:
                    raise DuplicateStudentError("Student with the same name already exists.")
            students.append(student_data)
            self.data_manager.save_data(students)
            return "Student added successfully."
    
    def delete_student(self, student_name):
        students = self.data_manager.load_data()
        initial_length = len(students)
        students = [student for student in students if student["name"] != student_name]
        if len(students) == initial_length:
            raise StudentNotFoundError("Student not found.")
        self.data_manager.save_data(students)
        return "Student deleted successfully."

    def update_marks(self, student_name, new_marks):
        if new_marks < 0 or new_marks > 100:
            raise InvalidMarksError("Invalid marks. Marks should be between 0 and 100.")
        else:
            students = self.data_manager.load_data()
            for student in students:
                if student["name"] == student_name:
                    student["marks"] = new_marks
                    self.data_manager.save_data(students)
                    return "Marks updated successfully."
            raise StudentNotFoundError("Student not found.")

    def get_all_students(self):
        return self.data_manager.load_data()