class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient balance")
    def get_balance(self):
        return self.__balance

acc = BankAccount(10000)
acc.deposit(2000)
acc.withdraw(3000)
print(acc.get_balance())

class User:
    def __init__(self, password):
        self.__password = password
    def login(self, password):
        if self.__password == password:
            print("Login successful")
        else:
            print("Invalid password")
    def change_password(self, old_password, new_password):
        if self.__password == old_password:
            self.__password = new_password
            print("Password changed successfully")
        else:
            print("Invalid old password")

u1 = User("password123")
u1.login("password123")
u1.change_password("password123", "newpassword")
u1.login("newpassword")