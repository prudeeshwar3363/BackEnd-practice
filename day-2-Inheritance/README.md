# 🔥 Day 2 – Inheritance & Polymorphism

## 📅 Date
(Enter today's date here)

---

## 🎯 Objective

Today’s focus was understanding and implementing:

- Inheritance in Python
- Parent and Child classes
- The `super()` keyword
- Method overriding
- Polymorphism
- Designing real-world class hierarchies

---

# 🧠 Concepts Learned

## 1️⃣ Inheritance

Inheritance allows a child class to reuse attributes and methods from a parent class.

It improves:
- Code reusability
- Structure
- Maintainability

Real-world backend examples:
- `User` → `AdminUser`
- `BankAccount` → `SavingsAccount`
- `Employee` → `FullTimeEmployee`

---

## 2️⃣ super() Keyword

Used to call the constructor of the parent class.

Example:

```python
super().__init__(name, age)
```

This ensures proper initialization without duplicating code.

---

## 3️⃣ Method Overriding

A child class modifies the behavior of a parent method.

Example:
- `SavingsAccount` overrides `withdraw()` to maintain minimum balance.

---

## 4️⃣ Polymorphism

Same method name but different behavior depending on the object.

Example:
Different employee types calculate salary differently using the same method name `calculate_salary()`.

---

# 🛠 Implementations

---

## 👤 Task 1 – Person → Student

### Parent Class: `Person`
Attributes:
- name
- age

Method:
- display_info()

### Child Class: `Student`
Additional Attribute:
- marks

Method:
- display_student_info()

### ✅ Sample Output

```
Name: Prudveeswar
Age: 21
Marks: 85
```

---

## 🏦 Task 2 – Bank System

### Parent Class: `BankAccount`
Attributes:
- account_holder
- balance

Methods:
- deposit()
- withdraw()
- display_balance()

### Child Class: `SavingsAccount`
Additional Attribute:
- interest_rate

Methods:
- calculate_interest()
- Overridden withdraw() with minimum balance rule

### ✅ Sample Output

```
Interest Amount: 500
Total Balance After Interest: 10500
```

### ❌ Minimum Balance Violation

```
Cannot withdraw! Minimum balance must be maintained.
```

---

## 👨‍💼 Mini Project – Employee Management System

### Parent Class: `Employee`
Attributes:
- name
- base_salary

Method:
- calculate_salary()

### Child 1: `FullTimeEmployee`
Additional Attribute:
- bonus

Salary Formula:
base_salary + bonus

### Child 2: `PartTimeEmployee`
Additional Attributes:
- hours_worked
- hourly_rate

Salary Formula:
hours_worked × hourly_rate

### ✅ Sample Output

```
60000
4000
```

---

# 🧩 Homework Completed

✔ User Role System (Admin & Customer)  
✔ Vehicle System with overridden `start_engine()`  
✔ Theory questions answered

---

# 💡 Key Takeaways

- Inheritance promotes code reuse.
- Method overriding allows customization of behavior.
- Polymorphism makes backend systems flexible and scalable.
- Backend frameworks like Django heavily use inheritance internally.

---

# 📈 Self Evaluation

Concept Clarity: ⭐⭐⭐⭐⭐  
Implementation Confidence: ⭐⭐⭐⭐☆  
Need More Practice On: Designing deeper class hierarchies

---

# 🏁 Status

✔ Day 2 Completed  
✔ Parent–Child Relationships Implemented  
✔ Method Overriding Practiced  
✔ Mini Project Built  

---

🚀 Ready for Day 3 – Encapsulation & Abstraction

