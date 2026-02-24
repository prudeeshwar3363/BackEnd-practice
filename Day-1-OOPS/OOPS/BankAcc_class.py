class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.deposited_amount = None
        self.withdrawn_amount = None

    def deposit(self, amount1):
        self.deposited_amount = amount1
        self.balance += amount1
    
    def withdraw(self, amount2):
        self.withdrawn_amount = amount2
        self.balance -= amount2
    
    def display_balance(self):
        print("-------------------------------------------------")
        if self.balance >= 0:
            print(f"Account Holder: {self.account_holder}")
            print(f"Deposited amount: {self.deposited_amount}")
            print(f"Withdrawn amount: {self.withdrawn_amount}")
            print(f"Current Balance: {self.balance}")
        else:
            print("Insufficient balance")

account_holder = input("Account Holder: ")
balance = int(input("Balance: "))
amount1 = int(input("Amount to deposit: "))
amount2 = int(input("Amount to withdraw: "))

b1 = BankAccount(account_holder, balance)
b1.deposit(amount1)
b1.withdraw(amount2)
b1.display_balance()