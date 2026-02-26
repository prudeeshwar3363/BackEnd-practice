# 🔐 Day 3 – Encapsulation & Abstraction

## 📅 Date
(Enter today's date here)

---

## 🎯 Objective

Today’s focus was on writing secure and professional class designs using:

- Encapsulation
- Private variables
- Getter & Setter methods
- Data validation
- Abstraction using ABC module

---

# 🧠 Concepts Learned

## 1️⃣ Encapsulation

Encapsulation is the practice of restricting direct access to sensitive data and controlling it using methods.

Used for:
- Protecting passwords
- Protecting balances
- Preventing unauthorized modifications

Private variables are defined using double underscore:

```python
self.__balance = balance
```

Access is controlled using getter and setter methods.

---

## 2️⃣ Getter & Setter Methods

Used to safely access and update private variables.

Benefits:
- Add validation
- Prevent invalid updates
- Improve security

---

## 3️⃣ Abstraction

Abstraction hides implementation details and exposes only necessary functionality.

Implemented using the `abc` module.

```python
from abc import ABC, abstractmethod
```

Abstract classes force child classes to implement required methods.

---

# 🛠 Implementations

---

## 🏦 Task 1 – Secure Bank Account

Private:
- __balance

Public Methods:
- deposit()
- withdraw()
- get_balance()

Validation:
- Cannot withdraw more than balance
- Balance cannot be accessed directly

### ✅ Sample Output

```
Balance after deposit: 12000
Balance after withdrawal: 9000
Current Balance: 9000
```

---

## 👤 Task 2 – Secure User System

Private:
- __password

Public Methods:
- login()
- change_password()

### ✅ Sample Output

```
Login Successful
Password Changed Successfully
Login Failed
```

---

## 💳 Task 3 – Payment System (Abstraction)

Abstract Class:
- Payment

Child Classes:
- CreditCardPayment
- UPIPayment

Each implements:
- pay(amount)

### ✅ Sample Output

```
Paid 500 using Credit Card
Paid 1000 using UPI
```

---

# 🧩 Homework Completed

✔ Employee class with private salary and validation  
✔ FileManager abstract class implemented  
✔ Theory questions answered in README

---

# 💡 Key Takeaways

- Encapsulation protects sensitive backend data.
- Getter/Setter methods allow controlled access.
- Abstraction forces proper system design.
- These concepts are heavily used in backend frameworks like Django.

---

# 📈 Self Evaluation

Concept Clarity: ⭐⭐⭐⭐⭐  
Implementation Confidence: ⭐⭐⭐⭐☆  
Need More Practice On: Designing layered abstraction systems

---

# 🏁 Status

✔ Day 3 Completed  
✔ Secure Class Systems Built  
✔ Abstract Classes Implemented  
✔ Backend-Level Thinking Strengthened  

---

🚀 Ready for Day 4 – Exception Handling (Production-Level Error Control)

