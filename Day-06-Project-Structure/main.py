from app.data_manager import DataManager
from app.service import StudentService

manager = DataManager("data/student.json")
service = StudentService(manager)

service.add_student({"name": "John", "marks": 90})
service.add_student({"name": "Alice", "marks": 85})

students = manager.load_data()
print(students)