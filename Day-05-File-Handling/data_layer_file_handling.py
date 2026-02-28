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

filename = "PYTHON BACK END/Day-05-File-Handling/student.json"
manager = DataManager(filename)
students = manager.load_data()
student_name = input("Enter student name: ")
student_marks = int(input("Enter student marks: "))
new_student = {"name": student_name, "marks": student_marks}
students.append(new_student)
manager.save_data(students)