class Laptop:
    def __init__ (self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price
        self.discounted_price = None
        self.percentage = None

    def apply_discount(self, percentage):
        self.percentage = percentage
        self.discounted_price = self.price - (self.price * (self.percentage / 100))
        return self.discounted_price

    def display_specs(self):
        print(f"Brand: {self.brand}")
        print(f"RAM: {self.ram}")
        print(f"Price: {self.price}")
        if self.discounted_price is not None:
            print(f"Price after {self.percentage}% discount: {self.discounted_price}")

brand = input("Brand: ")
ram = input("RAM: ")
price = int(input("Price: "))


l1 = Laptop(brand, ram, price)
l1.apply_discount(10)
l1.display_specs()