import json

class DataManager:
    def __init__(self, filename):
        self.filename = filename
    
    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def save_data(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)
    
    def add_student(self, student_name, student_marks):
        students = self.load_data()
        new_student = {"name": student_name, "marks": student_marks}
        students.append(new_student)
        self.save_data(students)
        return "Student added successfully!"

    def del_student(self, student_name):
        students = self.load_data()
        students = [student for student in students if student["name"] != student_name]
        self.save_data(students)
        return "Student deleted successfully!"
    
    def update_marks(self, student_name, new_marks):
        students = self.load_data()
        for student in students:
            if student["name"] == student_name:
                student["marks"] = new_marks
                break
        self.save_data(students)
        return "Marks updated successfully!"
    
    def view_students(self):
        students = self.load_data()
        if not students:
            return "No students found."
        return json.dumps(students, indent=4)

filename = "PYTHON BACK END/Day-05-File-Handling/student.json"
manager = DataManager(filename)
manager.add_student("John Doe", 85)
manager.add_student("Jane Smith", 92)
print(manager.view_students())
print("-"*60)
manager.del_student("John Doe")
print(manager.view_students())
print("-"*60)
manager.update_marks("Jane Smith", 95)
print(manager.view_students())