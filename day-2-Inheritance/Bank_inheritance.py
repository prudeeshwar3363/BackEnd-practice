class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")
    
    def display_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if self.balance-1000 >= amount:
            self.balance -= amount
        elif self.balance <= 1000 and amount > 0:
            print("Cannot withdraw! Minimum balance must be maintained.")
        else:
            print("Insufficient balance")

        
    
    def calculate_interest(self):
        print("Interest Amount:", int(self.balance*(self.interest_rate/100)))
        print("Total Balance After Interest:", int(self.balance+self.balance*(self.interest_rate/100)))

b1 = SavingsAccount("Prudveeswar", 10000, 5)

b1.withdraw(11000)
#b1.withdraw()
b1.calculate_interest()
b1.display_balance()