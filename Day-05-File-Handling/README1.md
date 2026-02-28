# 📂 Day 5 – File Handling & JSON

## 📅 Date
(Enter today's date)

---

# 🎯 What I Learned Today

Today I focused on understanding how backend systems store and retrieve data using files and JSON.

## 1️⃣ File Handling

I learned how to:
- Open files using different modes ("r", "w", "a")
- Use `with open()` for safe file handling
- Read content from files
- Write and append data
- Understand how overwriting happens in "w" mode

I understood why using `with open()` is considered best practice in backend development.

---

## 2️⃣ JSON Fundamentals

I learned:
- What JSON is and why it is used in backend systems
- JSON structure (list of dictionaries)
- Difference between `json.dump()` and `json.dumps()`
- How to use `json.load()` to read structured data
- Why an empty file causes `JSONDecodeError`

I understood that JSON must always contain valid structure like:

```
[]
```

for storing multiple records.

---

## 3️⃣ Backend Data Flow Thinking

I learned the correct flow for modifying stored data:

1. Load existing data
2. Modify it in memory
3. Save updated data back to file

This helped me understand why files were getting overwritten earlier.

---

## 4️⃣ Data Layer Separation (Very Important)

I built a `DataManager` class to:
- Load JSON data
- Save JSON data
- Handle file-related errors
- Separate storage logic from main application logic

This introduced me to the concept of separation of concerns, similar to how backend frameworks separate database logic from business logic.

---

# 🛠 What I Built Today

## 📝 1. Notes Manager
- Add notes
- View notes
- Store data in text file

## 🎓 2. Student JSON Storage System
- Add student
- View students
- Store multiple students in JSON
- Handle FileNotFoundError
- Handle JSONDecodeError

## 🏗 3. DataManager Class
- load_data()
- save_data()
- Structured data handling

## 🔥 Mini Project – JSON-Based Student Record System
- Add student
- Update marks
- Delete student
- View all students
- Persistent storage using JSON

---

# 💡 Key Realizations

- Backend systems must load data before modifying it.
- Overwriting happens if previous data is not loaded.
- JSON acts like a simple database.
- Separation of concerns makes systems scalable.
- File handling is slower compared to databases because files are not optimized for concurrent access.

---

# 📈 Self Evaluation

Concept Clarity: ⭐⭐⭐⭐⭐  
Implementation Confidence: ⭐⭐⭐⭐☆  
Need More Practice On: Designing scalable data layers and handling concurrent access issues

---

# 🏁 Status

✔ Day 5 Completed  
✔ JSON Persistence Implemented  
✔ DataManager Architecture Built  
✔ Backend Data Thinking Improved  

---

🚀 Moving to Day 6 – Virtual Environments & Professional Project Structuring

