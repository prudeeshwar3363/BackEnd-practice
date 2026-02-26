class Payment:
    def __init__(self):
        pass
    def pay(self, amount):
        pass
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using credit card")
class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

c1 = CreditCardPayment()
c1.pay(1000)
u1 = UPIPayment()
u1.pay(2000)