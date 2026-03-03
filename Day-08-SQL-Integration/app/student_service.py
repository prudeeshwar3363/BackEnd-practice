from app.database import DataBase
import sqlite3

class StudentService:
    def __init__(self):
        self.db = DataBase()
        self.db.create_table()

    def add_student(self, name, marks):
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", (name, marks))
            conn.commit()
        except sqlite3.IntegrityError:
            raise ValueError("Student already exists")
        conn.close()
        return "Student added successfully"
    def delete_student(self, name):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE name = ?", (name,))
        if cursor.rowcount == 0:
            conn.close()
            raise ValueError("Student not found")
        conn.commit()
        conn.close()
        return "Student deleted successfully"
    def update_marks(self, name, marks):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("UPDATE students SET marks = ? WHERE name = ?", (marks, name))
        if cursor.rowcount == 0:
            conn.close()
            raise ValueError("Student not found")
        conn.commit()
        conn.close()
        return "Marks updated successfully"
    def get_all_students(self):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        conn.close()
        return students