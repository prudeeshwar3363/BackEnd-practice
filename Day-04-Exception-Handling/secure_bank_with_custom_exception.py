class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Successfully withdrew {amount}. New balance: {self.balance}")

print("Initializing account with a balance of 1000.")
account = BankAccount(1000)

try:
    print("Attempting to withdraw 1500...")
    account.withdraw(1500)
except InsufficientBalanceError as e:
    print(f"Error: {e}")
    print(f"Transaction failed. Balance remains: {account.balance}")