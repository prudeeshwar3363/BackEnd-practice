import sqlite3

class DataBase:
    def __init__(self, db_name = "PYTHON BACK END/Day-08-SQL-Integration/data/students.db"):
        self.db_name = db_name
    
    def connect(self):
        return sqlite3.connect(self.db_name)
    
    def create_table(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            marks INTEGER NOT NULL
        )""")
        conn.commit()
        conn.close()