# 🗄 Day 8 – SQL Integration & Database Thinking

## 📅 Date
(Enter today's date)

---

# 🎯 Objective of Day 8

Today’s goal was to move from JSON-based storage to a real relational database using **SQLite** and SQL.

This day marks a major transition:

Flat file persistence ➝ Structured relational database

---

# 🧠 What I Learned Today

## 1️⃣ Understanding Relational Databases

I learned that relational databases store data in:

- Tables
- Rows
- Columns

Each row represents a record.
Each column represents a field.

Unlike JSON files, databases:
- Enforce constraints
- Prevent duplicates
- Support relationships
- Scale efficiently

---

## 2️⃣ SQL Core Commands (CRUD)

Today I practiced the foundation of backend data operations:

- `CREATE TABLE`
- `INSERT INTO`
- `SELECT`
- `UPDATE`
- `DELETE`

I understood how the `WHERE` clause is critical to prevent unintended updates or deletions.

---

## 3️⃣ Constraints & Data Integrity

Implemented and understood:

- `PRIMARY KEY`
- `AUTOINCREMENT`
- `UNIQUE`
- `NOT NULL`

The database now enforces rules automatically, reducing manual validation effort.

---

## 4️⃣ SQLite Integration with Python

Integrated SQLite using the `sqlite3` module.

Learned how to:

- Connect to database
- Execute SQL queries
- Commit transactions
- Close connections properly
- Handle `sqlite3.IntegrityError`

Also implemented parameterized queries using `?` to prevent SQL injection.

---

## 5️⃣ Replacing JSON with SQL (Major Shift)

Previously:

- Data stored in JSON file
- Manual validation
- No real constraints

Now:

- Data stored in `students.db`
- SQL table enforces constraints
- CRUD handled via queries
- Database-level validation active

Architecture remained layered — only the data layer changed.

This proves separation of concerns works.

---

# 🛠 What I Built Today

✔ Created SQLite database file  
✔ Created `students` table with constraints  
✔ Implemented full CRUD using SQL  
✔ Added UNIQUE constraint on student name  
✔ Handled duplicate insert errors  
✔ Integrated SQL with service layer  
✔ Maintained layered backend architecture  

---

# 🔍 Key Realizations

- Databases enforce integrity better than files.
- SQL constraints reduce bugs.
- Parameterized queries are essential for security.
- Backend systems rely heavily on structured relational storage.
- Clean architecture made migration from JSON to SQL simple.

---

# 📈 Self Evaluation

SQL Understanding: ⭐⭐⭐⭐☆  
Database Confidence: ⭐⭐⭐⭐☆  
Backend Growth: Significant  

---

# 🏁 Status

✔ Day 8 Completed  
✔ Successfully Migrated to Database Storage  
✔ Strengthened Database-Backed Backend Development Skills  

---

🚀 Ready to move into Advanced SQL & JOINS (Day 9).

